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
![image](https://github.com/github8585/exploratory-data-analysis---online-shopping-in-retail/assets/55400003/5ba507be-0a0a-4575-a5c4-e9817c2c82e8)

- Conducting exploratory data analysis, including handling null values, skewed columns, outliers, and correlation.
![image](https://github.com/github8585/exploratory-data-analysis---online-shopping-in-retail/assets/55400003/656f6734-aec5-47ba-b389-66ed5f02f8fc)

- Visualizing data distributions and correlations.
![image](https://github.com/github8585/exploratory-data-analysis---online-shopping-in-retail/assets/55400003/3da5ec02-2c31-4e05-857d-f73372d65eeb)

- Saving transformed data to a CSV file.
![image](https://github.com/github8585/exploratory-data-analysis---online-shopping-in-retail/assets/55400003/91f16d15-7546-4e29-91aa-9abe1bbe9255)

Throughout this project, I learned about data cleaning techniques, working with databases, data visualizations, and handling skewed data.

### Installation Instructions
1. Ensure you have the following Python libraries installed:
- `psycopg2`
- `sqlalchemy`
- `pandas`
- `yaml`
- `matplotlib`
- `seaborn`
- `scipy`
- `numpy`

2. Then import the following libraries installed:

![image](https://github.com/github8585/exploratory-data-analysis---online-shopping-in-retail/assets/55400003/cbee06d6-ecdb-44a2-8cea-04b9b20c78d2)

3. Clone the repository to your local machine.
```bash
git clone https://github.com/yourusername/Exploratory-data-analysis---online-shopping-in-retail.git
```

### Usage Instructions
1. Make sure you have a `credentials.yaml` file with your PostgreSQL database credentials.
```yaml
   RDS_HOST: 'your_host'
   RDS_PORT: 'your_port'
   RDS_DATABASE: 'your_database'
   RDS_USER: 'your_username'
   RDS_PASSWORD: 'your_password'
```

2. Run the script using the command:
- `python db_utils.py`

3. The script will extract the data, apply transformations, visualize the data, and then save the transformed data to `customer_activity_transformed_corrected_skew.csv`.

![image](https://github.com/github8585/exploratory-data-analysis---online-shopping-in-retail/assets/55400003/470152b4-14e3-4481-b871-ae89862e8824)

### File Structure
- Main script file: `db_utils.py`
- Database credentials: `credentials.yaml`
- Output transformed CSV: `customer_activity_transformed_corrected_skew.csv`

### License Information
This project is licensed under the MIT License. You can use, modify, and distribute this code freely. For more details, refer to the LICENSE file in the repository.

