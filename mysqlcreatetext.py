import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
from codecarbon import EmissionsTracker
# Function to insert text into to MySQL database
tracker = EmissionsTracker()
tracker.start()
def connect_to_mysql():
    try:
        conn_string = 'mysql+pymysql://root:admin@localhost/mysqlcreate'
        conn = mysql.connector.connect(user='root', passwd='admin', host='127.0.0.1', database='mysqlcreate')
        engine = create_engine(conn_string)
        print("Connected to MySQL database!")
        return engine
    except Exception as e:
        print("Error connecting to MySQL database:", e)
        return None

# Main function
def main():
    try:
        # Read data into Pandas DataFrame
        df = pd.read_csv('/Users/HP/Music/CRUD/dataset/sqlcsv.csv')

        # Connect to MySQL database
        engine = connect_to_mysql()
        if engine is None:
            return

        # Insert data into MySQL database
        table_name = 'Netflix'
        df.to_sql(table_name, engine, if_exists='append', index=False)

        print("Data inserted successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
emissions: float = tracker.stop()
print(emissions)