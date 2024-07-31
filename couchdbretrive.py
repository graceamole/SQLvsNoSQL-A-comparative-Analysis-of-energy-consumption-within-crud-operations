import couchdb

from codecarbon import EmissionsTracker
#code to retrive data
tracker = EmissionsTracker()
tracker.start()

def retrieve_all_documents(db):
    # Fetch all documents from the database
    result = db.view('_all_docs', include_docs=True,limit=760)
    
    # Delete each document
    for doc in result:
        print (doc)

# Connect to CouchDB server
server = couchdb.Server('http://admin:admin@localhost:5984/')

# Connect to the specific database
db_name = 'couchdb_createaudio'
db = server[db_name]

retrieve_all_documents(db)
emissions: float = tracker.stop()
print(emissions)