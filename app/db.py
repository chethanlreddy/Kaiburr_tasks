from pymongo import MongoClient
from pymongo.database import Database


mongo_db_connection_string = 'mongodb://localhost:27017'
client = MongoClient(mongo_db_connection_string)
db_name = 'dev_kaibur'
mongo_db: Database = client[db_name]
print(f'mongodb connected : {db_name}')

def get_mongo_db():
    try:
        yield mongo_db
    finally:
        pass