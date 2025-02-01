import pandas as pd
from sqlalchemy import create_engine

# Replace the following with your database connection details
username = 'root'  # Your MySQL username
password = '1234'  # Your MySQL password
host = 'localhost'  # Your MySQL host, e.g., 'localhost' or an IP address
database = 'cvr'  # Your MySQL database name

# Create a connection string using SQLAlchemy
connection_string = f'mysql+mysqlconnector://{username}:{password}@{host}/{database}'

# Create an engine
engine = create_engine(connection_string)

# Read data from MySQL into a pandas DataFrame
df_sql = pd.read_sql('SELECT * FROM student', engine)

# Display the DataFrame
print(df_sql)