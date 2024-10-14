import os
from pymongo import MongoClient

# MongoDB connection string (read from environment variable)
CONNECTION_STRING = os.getenv("MONGO_URI")

# Initially set the connection status and collection to None
isConnected = False
db_collection = None

# Database connection function
def ConnectDb():
    global isConnected, db_collection

    if isConnected:
        print("Already connected to the database")
    else:
        try:
            if CONNECTION_STRING is None:
                raise ValueError("MONGO_URI environment variable is not set")

            # Create MongoDB connection
            Mongo_connection = MongoClient(CONNECTION_STRING)
            db = Mongo_connection["notes_db"]  # Use the appropriate database name
            db_collection = db["notes"]  # Use the appropriate collection name
            isConnected = True  # Mark connection as established
            print("Successfully connected to the database")
            print(Mongo_connection)
            print(db_collection)

        except Exception as e:
            print(f"Failed to connect to the database: {e}")

# Test the connection
ConnectDb()
