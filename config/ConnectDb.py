import os
from pymongo import MongoClient
CONNECTION_STRING = os.getenv("MOGO_URI")  


isConnected = False 

def ConnectDb ():

  global isConnected

  if(isConnected):
    print("Already connected to the database")

  else:
      try:
        Mongo_connection = MongoClient(CONNECTION_STRING)
        isConnected = True
        print("Successfully connected to the database")
        print(Mongo_connection)

      except Exception as e:
        print(f"Failed to connect to the database , because of{e}") 


ConnectDb()