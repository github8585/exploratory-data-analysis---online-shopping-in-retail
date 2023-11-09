# Exploratory-data-analysis---online-shopping-in-retail

## RDSDatabaseConnector

### Table of Contents
- [Description](#description)
- [Installation](#installation)

### Description
The `RDSDatabaseConnector` project is a simple Python script that allows for the extraction of data from a PostgreSQL database, particularly an RDS instance. The aim of the project is to demonstrate how to use SQLAlchemy and Pandas to connect to a PostgreSQL database, fetch data, and save it to a CSV file. This project is an educational exercise in database connectivity, data extraction, and Python programming.

### Installation
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required Python packages if you haven't. You can install them using pip:
pip install pandas sqlalchemy pyyaml

4. Create a `credentials.yaml` file in the project directory and populate it with your PostgreSQL RDS instance credentials. The YAML file should have the following structure:

- `RDS_HOST: 'your_host'`
  
- `RDS_PORT: 'your_port'`
  
- `RDS_DATABASE: 'your_database'`
  
- `RDS_USER: 'your_username'`
  
- `RDS_PASSWORD: 'your_password'`

Open a terminal and navigate to the project directory.

Run the script using Python:

- `python db_utils.py`

A CSV file named customer_activity.csv containing data from the customer_activity table in your PostgreSQL database will be generated in the project directory.




