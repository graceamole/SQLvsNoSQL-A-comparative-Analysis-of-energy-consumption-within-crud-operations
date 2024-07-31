import mysql.connector
import os
from codecarbon import EmissionsTracker


# Connect to MySQL
conn = mysql.connector.connect(user='root', passwd='admin', host='127.0.0.1', database='mysqlcreate')

cursor = conn.cursor()

# Function to insert images into the database
def insert_images(folder_path):
    # Iterate through all files in the folder
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            try:
                with open(os.path.join(folder_path, filename), "rb") as file:
                    img_data = file.read()
                    
                    # Insert image data into the database
                    cursor.execute("insert into images(filename, file) VALUES (%s, %s)", (filename, img_data))
                    conn.commit()
                    print(f"{filename} inserted successfully.")
            except Exception as e:
                print(f"Error inserting {filename}: {e}")
tracker = EmissionsTracker()
tracker.start()
'''
def insert_audio(folder_path):
    # Iterate through all files in the folder
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp3") or filename.endswith(".mp4") or filename.endswith(".mp4"):
            try:
                with open(os.path.join(folder_path, filename), "rb") as file:
                    audio_data = file.read()
                    
                    # Insert image data into the database
                    cursor.execute("insert into audio(filename, file) VALUES (%s, %s)", (filename, audio_data))
                    conn.commit()
                    print(f"{filename} inserted successfully.")
            except Exception as e:
                print(f"Error inserting {filename}: {e}")'''

# Path to the folder containing images
folder_path = "/Users/HP/Music/CRUD/image/"
#folder_path = "/Users/HP/Music/CRUD/audio/"
#insert_images(folder_path)
insert_images(folder_path)
emissions: float = tracker.stop()
print(emissions)
# Close the cursor and connection
cursor.close()
conn.close()