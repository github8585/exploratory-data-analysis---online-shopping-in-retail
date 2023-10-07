import psycopg2  # Assuming you are using a PostgreSQL RDS instance
from typing import List, Optional
from sqlalchemy import create_engine
import pandas as pd 
import yaml 

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
    save_data_to_csv(data_frame, 'customer_activity.csv')

