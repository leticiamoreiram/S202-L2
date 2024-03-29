from typing import Collection
import pymongo


# with open('data.json',encoding='utf8') as f:
#     dataset = json.load(f)


class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connectionString = "localhost:27017"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Database connected successfully!")
        except Exception as e:
            print(e)

    def reset_database(self):
        try:
            self.db.drop_collection(self.collection)
            #self.collection.insert_many(dataset)
            print("Database reseted successfully!")
        except Exception as e:
            print(e)