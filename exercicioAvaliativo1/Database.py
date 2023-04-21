import pymongo

class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connectionString = "mongodb+srv://leticiamoreiram:<senha123>@cluster0.d5hr6y7.mongodb.net/test"
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