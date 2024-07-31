import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import pandas as pd
from codecarbon import EmissionsTracker

conn = psycopg2.connect( 
        host='localhost',
        dbname = 'postgrescreate2',
        user = 'postgres',
        password='admin',
        port = 5432)
tracker = EmissionsTracker()
tracker.start()

# Function to connect to PostgreSQL database to create text
def connect_to_postgres():
    try:
        conn_string = 'postgresql://postgres:admin@localhost:5432/postgrescreate2'
        engine = create_engine(conn_string)
        print("Connected to PostgreSQL database!")
        return engine
    except Exception as e:
        print("Error connecting to PostgreSQL database:", e)
        return None

# Main function
def main():
    try:
        # Read data into Pandas DataFrame 
        df = pd.read_csv('/Users/HP/Music/CRUD/dataset/sqlcsv.csv')

        # Connect to PostgreSQL database
        engine = connect_to_postgres()
        if engine is None:
            return

        # Insert data into PostgreSQL database
        table_name = 'netflix'  # Change this to your table name in PostgreSQL
        df.to_sql(table_name, engine, if_exists='append', index=False)

        print("Data inserted successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
    emissions: float = tracker.stop()
    print(emissions)