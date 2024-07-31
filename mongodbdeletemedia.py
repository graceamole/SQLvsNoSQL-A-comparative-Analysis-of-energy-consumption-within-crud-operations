from pymongo import MongoClient
import pymongo

from codecarbon import EmissionsTracker
#code to delete data in mongodb
#tracker = EmissionsTracker()
#tracker.start()
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mongodatabase"]

count = 0

def delete_images():
    n = 50
    cursor = collection.find().limit(n)
    collection = db["mongodb_insertaudio"]
    count = 0
    try:
        # Delete all documents in the collection
        for document in cursor:
            id = document.get("_id")

            delete_query = {"_id": id}
            collection.delete_one(delete_query)
            count=count+1 
        print(f"{count} documents deleted successfully.")        
    except Exception as e:
        print(f"Error deleting documents: {e}")

def delete_text():
    n = 6
    collection = db["mongodb_insertaudio.chunks"]
    cursor = collection.find()
    count = 0
    try:
        # Delete all documents in the collection
        for document in cursor:
            id = document.get("_id")

            delete_query = {"_id": id}
            collection.delete_one(delete_query)
            count=count+1 
        print(f"{count} documents deleted successfully.")        
    except Exception as e:
        print(f"Error deleting documents: {e}")

delete_text()
#emissions: float = tracker.stop()
#print(emissions)





