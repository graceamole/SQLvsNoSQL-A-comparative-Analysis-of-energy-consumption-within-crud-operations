#code to convert the data in csv and insert into the couch db database
import couchdb
import pandas as pd
from codecarbon import EmissionsTracker


server = couchdb.Server('http://admin:admin@localhost:5984/')
tracker = EmissionsTracker()
tracker.start()
#db=server.create('couchdb_inserttext2')
db = server['couchdb_insert_text']
df =pd.read_csv("/Users/HP/Music/CRUD/dataset/sqlcsv.csv")
data= df.to_dict(orient = "records")
for doc in data:
        db.save(doc)
        print('insertingdata')


emissions: float = tracker.stop()
print(emissions)