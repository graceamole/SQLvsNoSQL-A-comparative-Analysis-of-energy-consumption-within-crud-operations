#code to retrieve records from mongodb
from pymongo import MongoClient
import pymongo
from codecarbon import EmissionsTracker
tracker = EmissionsTracker()
tracker.start()
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mongodatabase"]
collection = db["mongodb_insertpictures"]
cursor= collection.find()
count= 0
for doc in cursor:
     count=count+1
     print(doc)
     
print(count)
emissions: float = tracker.stop()
print(emissions)
