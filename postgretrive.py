import psycopg2

from psycopg2 import Binary
from codecarbon import EmissionsTracker

conn = psycopg2.connect( 
            host='localhost',
            dbname = 'postgrescreate2',
            user = 'postgres',
            password='admin',
            port = 5432)
tracker = EmissionsTracker()
tracker.start()

cur = conn.cursor()

# table name
table_name = "netflix"

# Define the SQL query to update 5 columns
sql_query = """
    UPDATE {} 
    SET type= %s, title = %s, country = %s, rating = %s, duration = %s
""".format(table_name)


# Define new values for the 5 columns
new_values = ('masters10', 'Green networking10', 'united kingdom10', 'good10', '12 months10')

# Execute the SQL query
cur.execute(sql_query, new_values)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
conn= conn.cursor() 

#code to retrive data from mysql
sql = "SELECT * from  images"
sql3 = "SELECT * from netflix LIMIT  10000"
sql2 = "SELECT * FROM images LIMIT 50"
sql5 = "SELECT * FROM images "
sql4 ="DELETE FROM netflix ORDER BY show_id LIMIT 10000"
conn.execute(sql5)
images= conn.fetchall()
print(images)
emissions: float = tracker.stop()
print(emissions)
conn.close


