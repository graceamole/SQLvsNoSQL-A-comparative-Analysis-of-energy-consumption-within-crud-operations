#code to inser images into a couchdb database
import couchdb
import os
import couchdb
import base64
import os
from codecarbon import EmissionsTracker
# Connect to CouchDB server
server = couchdb.Server('http://admin:admin@localhost:5984/')


#tracker = EmissionsTracker()
#tracker.start()
# Create or connect to a specific database
db_name = 'image_database'
try:
    db = server.create(db_name)
except couchdb.http.PreconditionFailed:
    db = server[db_name] # 

def encode_image(file_path):
    with open(file_path, 'rb') as f:
        encoded_image = base64.b64encode(f.read()).decode('utf-8')
    return encoded_image

# Path to the folder containing the images
folder_path = '/Users/HP/Music/CRUD/image'

# Iterate through the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.png') or filename.endswith('.jpeg'):  # Assuming images are in JPG or PNG format
        file_path = os.path.join(folder_path, filename)
        # Read the image file and encode it into base64
        image_data = encode_image(file_path)
        # Create a document with the image data and any metadata
        doc = {
            'filename': filename,
            'data': image_data,
        }
        # Save the document to the CouchDB database
        db.save(doc)
#emissions: float = tracker.stop()
#print(emissions)
