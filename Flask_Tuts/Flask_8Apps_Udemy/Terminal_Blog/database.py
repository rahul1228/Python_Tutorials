import pymongo

class Database(object):

    # ++GLOBAL VARS = ALL DATABASE OBJECTS CREATED SHARE THESE VARS++
    # Global vars are accessed by Database. vs self.
    # Only Static functions/Methods can access global vars
    URI = "mongodb://127.0.0.1:27017" # database host and host port
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI) # MongoClient function from pymongo
        Database.DATABASE = client['fullstack']

    def insert(collection, data):
        Database.DATABASE[collection].insert(data)