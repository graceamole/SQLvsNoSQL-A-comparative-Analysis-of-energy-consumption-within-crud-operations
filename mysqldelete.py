import mysql.connector
from codecarbon import EmissionsTracker

#code to delete data from mysql database
#establishing the connection
conn = mysql.connector.connect(user='root', passwd='admin', host='127.0.0.1', database='mysqlcreate')
tracker = EmissionsTracker()
tracker.start()
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
#sql = "Delete  from images where id = 4 "
sql2 = "DELETE FROM audio ORDER BY id LIMIT 760"
#sql4 = "DELETE FROM netflix ORDER BY show_id  LIMIT 10000"
#sql4 = "DELETE from images "
cursor.execute(sql2)
print('delected succesfully ')
emissions: float = tracker.stop()
print(emissions)
conn.commit()


#Closing the connection
conn.close()