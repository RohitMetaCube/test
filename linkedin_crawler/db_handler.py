from pymongo import MongoClient
import config

class MongoController:
    def __init__(self):
        client = MongoClient(config.MONGODB_HOST, config.MONGODB_PORT)
        self.db = client[config.DB_NAME]
     
    def ensure_indexes(self, collection_name):
        self.db[collection_name].ensure_index('user_name')
        self.db[collection_name].ensure_index('url')
        self.db[collection_name].ensure_index('user_type')
        
    def insert_into_db(self, collection_name, records):
        self.db[collection_name].insert(records)