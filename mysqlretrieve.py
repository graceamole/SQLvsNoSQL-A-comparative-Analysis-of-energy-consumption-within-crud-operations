import mysql.connector
from codecarbon import EmissionsTracker
#establishing the connection
conn = mysql.connector.connect(user='root', passwd='admin', host='127.0.0.1', database='mysqlcreate')

#Creating a cursor object using the cursor() method
cur = conn.cursor()
tracker = EmissionsTracker()
tracker.start()


#code to retrive data from mysql database
#Executing an MYSQL function using the execute() method
sql= "SELECT  * from images"
sql2 = "SELECT file_name FROM audio LIMIT 819"
sql3 = "SELECT * FROM netflix LIMIT 10000"
#cur.execute(sql)
#images= cur.fetchall()
#print(images)
# Fetch a single row using fetchone() method.



table_name = "netflix"


new_values = ('masters10', 'Green networking10', 'united kingdom10', 'good10', '12 months10')

# Define the SQL query to update 5 columns

sql_query = """
    UPDATE netflix 
    SET type = %s, title= %s, country = %s, rating = %s, duration = %s
"""

# Define new values for the 5 columns
new_values = ('masters9', 'Green networking9', 'united kingdom9', 'good9', '12 months9')

# Execute the SQL query 
cur.execute(sql_query, new_values)
conn.commit()
print('update done')

# Close the cursor and connection
emissions: float = tracker.stop()
print(emissions)
#Closing the connection
conn.close()