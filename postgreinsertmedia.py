import os
import psycopg2
from psycopg2 import Binary
from codecarbon import EmissionsTracker

tracker = EmissionsTracker()
tracker.start()
# Function to insert image into the postgress database


def insert_image(image_path,filename,conn):
    try:
        with conn.cursor() as cursor:
            with open(image_path,'rb') as f:
                image_data = f.read()
                filename=filename
            cursor.execute("INSERT INTO images (filename,image_data) VALUES (%s,%s);", (filename,Binary(image_data),))
            conn.commit()
        print(f"Image {image_path} inserted successfully!")
    except psycopg2.Error as e:
        print(f"Error inserting image {image_path}:", e)

# Main function
def main():
    try:
        # Connect to your PostgreSQL database
        conn = psycopg2.connect(
            host='localhost',
            dbname = 'postgrescreate2',
            user = 'postgres',
            password='admin',
            port = 5432
        )


        # Create a table to store images if not exists
        with conn.cursor() as cursor:
            cursor.execute("""
                    CREATE TABLE IF NOT EXISTS images (
                        id SERIAL PRIMARY KEY,
                        filename text,
                        image_data BYTEA
                    );
                """)
            conn.commit()


        # Directory containing images
        image_folder = "/Users/HP/Music/CRUD/image"

        # Insert images into the database
        for filename in os.listdir(image_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                filename = filename
                image_path = os.path.join(image_folder, filename)
                insert_image(image_path,filename, conn)

    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL:", e)
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    main()
    emissions: float = tracker.stop()

    print(emissions)
