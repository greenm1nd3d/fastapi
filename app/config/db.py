from pymongo import MongoClient
from decouple import config

DB_CONNECTION = config("DB_CONNECTION")

client = MongoClient(DB_CONNECTION)

db = client.tasks

tasks_collection = db["tasks"]
users_collection = db["users"]
