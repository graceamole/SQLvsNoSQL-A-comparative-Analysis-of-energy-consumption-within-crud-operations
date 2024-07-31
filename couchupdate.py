#code to update data in couchhdb
import couchdb
from codecarbon import EmissionsTracker
# Connect to CouchDB server
couch = couchdb.Server('http://admin:admin@localhost:5984/')
db_name = 'couchdb_inserttext' 
db = couch[db_name]
tracker = EmissionsTracker()
tracker.start()

# Define the new information for 5 columns
new_info = {
    'type': 'master10',
    'title': 'Green networking10',
    'country': 'united kingdom10',
    'rating': 'good10',
    'duration': '12 months10'
}

# Iterate over all documents in the database and update them
for doc_id in db:
    doc = db[doc_id]
    for key, value in new_info.items():
        doc[key] = value
    db[doc_id] = doc

print("Information updated successfully.")
emissions: float = tracker.stop()
print(emissions)








