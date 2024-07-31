import psycopg2

from psycopg2 import Binary
from codecarbon import EmissionsTracker
#code to delete data from  postgress
conn = psycopg2.connect( 
            host='localhost',
            dbname = 'postgrescreate',
            user = 'postgres',
            password='admin',
            port = 5432)
tracker = EmissionsTracker()
tracker.start()
cur = conn.cursor() 

cur.execute ('''DELETE FROM audio
            WHERE id IN (
            SELECT id
            FROM audio
            ORDER BY id
            LIMIT 760
           );
            ''')


#cur.execute(sql5)
conn.commit()
print('delected succesfully ')
emissions: float = tracker.stop()
print(emissions)
cur.close()
conn.close()   
