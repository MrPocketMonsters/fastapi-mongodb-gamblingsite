import os
from pymongo import MongoClient

client = MongoClient(os.environ.get('MONGODB_URI'))

db = client.gamblingsite_db

users_collection = db.get_collection('users')
