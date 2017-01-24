import pymongo

class Database(object):

    # ++GLOBAL VARS = ALL DATABASE OBJECTS CREATED SHARE THESE VARS++
    # Global vars are accessed by Database. vs self.
    # Only Static functions/Methods can access global vars
    URI = "mongodb://127.0.0.1:27017" # database host and host port
    DATABASE = None

    # Connects to client database at URI host url & port.
    # Then database collection is selected stored in DATABASE global var
    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI) # MongoClient function from pymongo
        Database.DATABASE = client['fullstack']

    # inserts data to a database collection
    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)  # .insert()function = from pymongo

    # Queries for data in a database collection
    # returns a pymongo cursor id
    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query) # .find() function = from pymongo

    # Queries for data in a database collection
    # returns that data, aka a json object or post info, from mongodb
    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)  # .find_one() function = from pymongo