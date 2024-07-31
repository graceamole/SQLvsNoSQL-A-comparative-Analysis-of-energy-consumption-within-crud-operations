#code to insert images and audio into mongodb
import os
from pymongo import MongoClient
from bson import Binary
import gridfs
from codecarbon import EmissionsTracker

from PIL import Image
#tracker = EmissionsTracker()
#tracker.start()

# Function to connect to MongoDB and insert image data
def insert_images(image_folder, db_name, collection_name):
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client[db_name]
    collection = db[collection_name]

    # Iterate over images in the folder
    
    for filename in os.listdir(image_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # Adjust file extensions as necessary
            image_path = os.path.join(image_folder, filename)
            with open(image_path, 'rb') as f:
                image_data = f.read()
            # Insert image data into MongoDB
            image_document = {
                "filename": filename,
                "image_data": Binary(image_data)
            }
            collection.insert_one(image_document)
            print(f"Inserted {filename} into MongoDB") 

def insert_audio(audio_folder, db_name, acollection_name):
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client[db_name]
    collection = db[acollection_name]

    #Iterate over audio in the folder
    for filename in os.listdir(audio_folder):
        if filename.endswith(".mp3") or filename.endswith(".mp4"):  
            audio_path = os.path.join(audio_folder, filename)
            with open(audio_path, 'rb') as f:
                audio_data = f.read()
            # Insert image data into MongoDB
            audio_document = {
                "filename": filename,
              "image_data": Binary(audio_data)
            }
            collection.insert_one(audio_document)
            print(f"Inserted {filename} into MongoDB")


image_folder = "/Users/HP/Music/CRUD/image"  
db_name = "mongodatabase"  
collection_name = "mongodb_insertpictures"  
audio_folder = "/Users/HP/Music/CRUD/audio"
acollection_name = "mongodb_insertaudio"  


insert_images(image_folder, db_name, collection_name)
insert_audio(audio_folder, db_name, acollection_name)
#emissions: float = tracker.stop()

#print(emissions)

    