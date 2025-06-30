from pymongo import MongoClient

def get_mongo_client():
    client = MongoClient("mongodb://mongo:27017/")
    return client["quitogo_reservations_db"]
