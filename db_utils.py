import psycopg2
from typing import List, Optional
from sqlalchemy import create_engine
import pandas as pd
import yaml
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import numpy as np 

class DataTransform:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def convert_to_categorical(self, columns: List[str]):
        for col in columns:
            self.df[col] = self.df[col].astype('category')

    def apply_transformations(self):
        categorical_columns = ['month', 'operating_systems', 'browser', 'region', 'traffic_type', 'visitor_type']
        self.convert_to_categorical(categorical_columns)


class DataFrameInfo:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def describe_columns(self) -> pd.Series:
        return self.df.dtypes

    def extract_statistical_values(self) -> pd.DataFrame:
        return self.df.describe(include='all').loc[['mean', 'std', '50%']]

    def count_distinct_values(self) -> pd.Series:
        return self.df.select_dtypes(include=['category']).nunique()

    def print_shape(self):
        return self.df.shape

    def count_null_values(self) -> pd.Series:
        null_count = self.df.isnull().sum()
        null_percentage = (self.df.isnull().sum() / len(self.df)) * 100
        return pd.DataFrame({'Count': null_count, 'Percentage (%)': null_percentage})


class Plotter:
    def plot_null_removal(self, before: pd.Series, after: pd.Series):
        df = pd.DataFrame({'Before': before, 'After': after})
        df.plot(kind='bar', figsize=(10, 5))
        plt.title('Null Value Removal')
        plt.xlabel('Columns')
        plt.ylabel('Null Value Count')
        plt.show()
    
    def visualize_data_distribution(self, df: pd.DataFrame, columns: List[str]):
        for col in columns:
            sns.kdeplot(df[col], fill=True)
            plt.title(f'Distribution for {col}')
            plt.show()


class DataFrameTransform(DataFrameInfo):
    def drop_columns(self, columns: List[str]):
        self.df.drop(columns=columns, inplace=True)

    def impute_columns(self):
        for col in self.df.columns:
            if self.df[col].isnull().sum() > 0:
                if self.df[col].dtype == 'object' or self.df[col].dtype.name == 'category':
                    self.df[col].fillna(self.df[col].mode()[0], inplace=True)
                else:
                    if self.df[col].dtype in ['int64', 'float64']:
                        if self.df[col].skew() > 1:
                            self.df[col].fillna(self.df[col].median(), inplace=True)
                        else:
                            self.df[col].fillna(self.df[col].mean(), inplace=True)

    def identify_skewed_columns(self, threshold: float = 0.5) -> List[str]:
        numeric_cols = self.df.select_dtypes(include=['int64', 'float64'])
        skewed_cols = numeric_cols.columns[numeric_cols.skew().abs() > threshold].tolist()
        return skewed_cols

    def transform_skewed_columns(self, columns: List[str]):
        for col in columns:
          if self.df[col].min() > 0:
            try:
                self.df[col], _ = stats.boxcox(self.df[col])
            except:
                print(f"Could not transform {col} using boxcox.")
            else:
                try:
                    self.df[col], _ = stats.yeojohnson(self.df[col])
                except:
                    print(f"Could not transform {col} using yeojohnson.")
    
    def handle_outliers(self, columns: List[str], method="IQR"):
        for col in columns:
            if method == "IQR":
                Q1 = self.df[col].quantile(0.25)
                Q3 = self.df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                self.df = self.df[(self.df[col] >= lower_bound) & (self.df[col] <= upper_bound)]
    
    def compute_correlation_matrix(self):
        return self.df.corr(numeric_only=True)

    def visualize_correlation_matrix(self, matrix):
        plt.figure(figsize=(15, 10))
        sns.heatmap(matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
        plt.title("Correlation Matrix")
        plt.show()

    def identify_highly_correlated_columns(self, threshold=0.9):
        corr_matrix = self.df.corr(numeric_only=True).abs()
        upper_triangle = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool_))
        to_drop = [column for column in upper_triangle.columns if any(upper_triangle[column] > threshold)]
        return to_drop

    def remove_columns(self, columns: List[str]):
        self.df.drop(columns=columns, inplace=True)
    
class RDSDatabaseConnector:
    def __init__(self, credentials: dict):
        self.host = credentials['RDS_HOST']
        self.port = credentials['RDS_PORT']
        self.dbname = credentials['RDS_DATABASE']
        self.user = credentials['RDS_USER']
        self.password = credentials['RDS_PASSWORD']
        self.connection = None

    def create_engine(self):
        url = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}"
        self.engine = create_engine(url)

    def extract_data(self, table_name: str) -> pd.DataFrame:
        query = f"SELECT * FROM {table_name};"
        data_frame = pd.read_sql(query, self.engine)
        return data_frame


def save_data_to_csv(data_frame: pd.DataFrame, filename: str):
    data_frame.to_csv(filename, index=False)


def load_db_credentials(filepath='credentials.yaml') -> dict:
    with open(filepath, 'r') as file:
        credentials = yaml.safe_load(file)
    return credentials


if __name__ == "__main__":
    credentials = load_db_credentials()
    connector = RDSDatabaseConnector(credentials)
    connector.create_engine()
    data_frame = connector.extract_data('customer_activity')

    transformer = DataTransform(data_frame)
    transformer.apply_transformations()

    eda_transform = DataFrameTransform(data_frame)

    null_values_before = eda_transform.count_null_values()['Count']
    print("Null Values Before:", null_values_before)

    eda_transform.impute_columns()

    null_values_after = eda_transform.count_null_values()['Count']
    print("Null Values After:", null_values_after)

    plotter = Plotter()
    plotter.plot_null_removal(null_values_before, null_values_after)

    skewed_cols = eda_transform.identify_skewed_columns()
    numeric_cols = data_frame.select_dtypes(include=['int64', 'float64']).columns.tolist()

    plotter.visualize_data_distribution(data_frame, numeric_cols)

    eda_transform.handle_outliers(numeric_cols)

    plotter.visualize_data_distribution(data_frame, numeric_cols)

    for col in skewed_cols:
        sns.kdeplot(data_frame[col], label='Before Skew Transformation', fill=True)

    eda_transform.transform_skewed_columns(skewed_cols)

    for col in skewed_cols:
        sns.kdeplot(data_frame[col], label='After Skew Transformation', fill=True)
        plt.legend()
        plt.show()
    
    correlation_matrix = eda_transform.compute_correlation_matrix()
    eda_transform.visualize_correlation_matrix(correlation_matrix)

    columns_to_remove = eda_transform.identify_highly_correlated_columns()

    eda_transform.remove_columns(columns_to_remove)

    save_data_to_csv(data_frame, 'customer_activity_transformed_corrected_skew.csv')
 