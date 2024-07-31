import os
import psycopg2
from psycopg2 import Binary
from codecarbon import EmissionsTracker

tracker = EmissionsTracker()
tracker.start()
# Function to insert audio into the  postgress database


def insert_audio(audio_path,filename,conn):
    try:
        with conn.cursor() as cursor:
            with open(audio_path,'rb') as f:
                audio_data = f.read()
                filename=filename
            cursor.execute("INSERT INTO audio (filename,audio_data) VALUES (%s,%s);", (filename,Binary(audio_data),))
            conn.commit()
        print(f"audio {audio_path} inserted successfully!")
    except psycopg2.Error as e:
        print(f"Error inserting audio {audio_path}:", e)

# Main function
def main():
    try:
        # Connect to your PostgreSQL database
        conn = psycopg2.connect(
            host='localhost',
            dbname = 'postgrescreate',
            user = 'postgres',
            password='admin',
            port = 5432
        )


        # Create a table to store images if not exists
        with conn.cursor() as cursor:
            cursor.execute("""
                    CREATE TABLE IF NOT EXISTS audio (
                        id SERIAL PRIMARY KEY,
                        filename text,
                        audio_data BYTEA
                    );
                """)
            conn.commit()


        # Directory containing images
        audio_folder = "/Users/HP/Music/CRUD/audio"

        # Insert images into the database
        for filename in os.listdir(audio_folder):
            if filename.endswith(('.mp3', '.mp4')):
                filename = filename
                audio_path = os.path.join(audio_folder, filename)
                insert_audio(audio_path,filename, conn)

    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL:", e)
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    main()
    emissions: float = tracker.stop()
    print(emissions)

    
