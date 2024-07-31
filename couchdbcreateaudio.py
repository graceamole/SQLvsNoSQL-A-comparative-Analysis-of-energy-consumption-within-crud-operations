#code to insert audio into couchdb
import os
import couchdb
import base64
from codecarbon import EmissionsTracker
# Connect to CouchDB server
server = couchdb.Server('http://admin:admin@localhost:5984/')
#tracker = EmissionsTracker()
#tracker.start()
# Create or connect to a specific database
db_name = 'couchdb_createaudio'
try:
    db = server.create(db_name)
except couchdb.http.PreconditionFailed:
    db = server[db_name]  

# Path to the folder containing audio files
audio_folder = '/Users/HP/Music/CRUD/audio'
tracker = EmissionsTracker()
tracker.start()
# Iterate over each audio file in the folder
for filename in os.listdir(audio_folder):
    if filename.endswith('.mp3') or filename.endswith('.mp4'):
        filepath = os.path.join(audio_folder, filename)
        
        # Read the audio file
        with open(filepath, 'rb') as file:
            audio_data = file.read()
        
        # Encode the audio data in base64 format
   
        encoded_audio = base64.a85encode(audio_data).decode('utf-8')
        
        # Create a document and insert it into the database
        doc = {
            'filename': filename,
            'audio': encoded_audio,
        }
        db.save(doc)
        print(f"Inserted {filename} into the database.")

#emissions: float = tracker.stop()
#print(emissions)