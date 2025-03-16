from pymongo import MongoClient

class MongoDB:
    def __init__(self, db_name: str, host: str = "localhost", port: int = 27017):
        # Connect to MongoDB
        try:
            self.client = MongoClient(host, port)
            self.db = self.client[db_name]  # Access the specified database
            print(f"Connected to MongoDB database: {db_name}")
        except ConnectionError as e:
            print(f"Error connecting to MongoDB: {e}")
            self.client = None
            self.db = None
