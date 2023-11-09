# Exploratory-data-analysis---online-shopping-in-retail

## Data Analysis and Transformation for Customer Activity

### Table of Contents
- [Project Description](#project-description)
- [Installation Instructions](#installation-instructions)
- [Usage Instructions](#usage-instructions)
- [File Structure](#file-structure)
- [License Information](#license-information)

### Project Description
This project aims to conduct data analysis and transformations on customer activity data. The main functionalities include:
- Extracting data from a PostgreSQL database.
- Conducting exploratory data analysis, including handling null values, skewed columns, outliers, and correlation.
- Visualizing data distributions and correlations.
- Saving transformed data to a CSV file.

Throughout this project, I learned about data cleaning techniques, working with databases, data visualizations, and handling skewed data.

### Installation Instructions
Ensure you have the following Python libraries installed:
- `psycopg2`
- `sqlalchemy`
- `pandas`
- `yaml`
- `matplotlib`
- `seaborn`
- `scipy`
- `numpy`

Clone the repository to your local machine.

### Usage Instructions
1. Make sure you have a `credentials.yaml` file with your PostgreSQL database credentials.
2. Run the script using the command:
- `python db_utils.py`

3. The script will extract the data, apply transformations, visualize the data, and then save the transformed data to `customer_activity_transformed_corrected_skew.csv`.

### File Structure
- Main script file: `db_utils.py`
- Database credentials: `credentials.yaml`
- Output transformed CSV: `customer_activity_transformed_corrected_skew.csv`

### License Information
This project is licensed under the MIT License. You can use, modify, and distribute this code freely. For more details, refer to the LICENSE file in the repository.

