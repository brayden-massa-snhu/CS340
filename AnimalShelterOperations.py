from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'aacpassword'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32585
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        try:
            if data:
                self.collection.insert_one(data)
                return True
            else:
                raise ValueError("Data parameter is empty")
        except Exception as e:
            print(f"An error occured: {e}")
            return False

# Create method to implement the R in CRUD.
    def read(self, query):
        try:
            cursor = self.collection.find(query)
            return list(cursor)
        except Exception as e:
            print(f"An error has occured: {e}")
            return []
# Update method to implement the U in CRUD.
    def update(self, query, data):
        try:
            if not query or not data:
                raise ValueError("Query or data parameter is empty")
            result = self.collection.update_many(query, {'$set': data})
            return result.modified_count
        except Exception as e:
            print(f"An error has occured: {e}")
            return 0

# Delete method to implement the D in CRUD.
    def delete(self, query):
        try:
            if not query:
                raise ValueError("Query parameter is empty")
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"An error has occured: {e}")
            return 0