import pymongo
from codecarbon import EmissionsTracker

tracker = EmissionsTracker()
tracker.start()
# Establish connection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["mongodatabase"]
collection = database["mongodb_create"]  

# Define the update query to specify the fields and their new values
update_query = {
    '$set': {
        'type': 'master3',
        'title': 'Green networking3',
        'country': 'united kingdom3',
        'rating': 'good3',
        'duration': '12 months3'
    }
}

# Update the documents matching the filter with the new values
result = collection.update_many({}, update_query)
# Print the number of documents updated
print("Number of documents updated:", result.modified_count)
emissions: float = tracker.stop()
print(emissions)