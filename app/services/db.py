import os
from pymongo import MongoClient

db_client = MongoClient(os.environ['MONGO_URI'])
print("Connecting to db...")
database = db_client.minichallenge
print(database)
