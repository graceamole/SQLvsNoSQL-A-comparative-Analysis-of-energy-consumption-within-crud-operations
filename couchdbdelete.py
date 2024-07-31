import couchdb
#code to delete data from couch db
from codecarbon import EmissionsTracker
# Connect to CouchDB server
server = couchdb.Server('http://admin:admin@localhost:5984/')

tracker = EmissionsTracker()
tracker.start()

# Connect to the specific database
db_name = 'couchdb_createaudio'
db = server[db_name]
def delete_all_documents(db):
    # Fetch all documents from the database
    result = db.view('_all_docs', include_docs=True,limit=760)
    
    # Delete each document
    for row in result:
        db.delete(row.doc)
        print('delected')

# Delete all documents from the database
delete_all_documents(db)

emissions: float = tracker.stop()
print(emissions)