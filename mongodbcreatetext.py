#code to insert data from csv into mongodb
import pymongo
import json
import pandas as pd
from codecarbon import EmissionsTracker

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#tracker = EmissionsTracker()
#tracker.start()

db = myclient["mongodatabase"]  # Name of the MongoDB database
collection = db["mongodb_create"] # Name of the collection within the database
df =pd.read_csv("/Users/HP/Music/CRUD/dataset/sqlcsv.csv")
data= df.to_dict(orient = "records")
collection.insert_many(data)

#emissions: float = tracker.stop()
#print(emissions)