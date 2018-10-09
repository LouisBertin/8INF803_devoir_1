from pymongo import MongoClient


def string_between_two_others(start, end, string):
    s = str(string)
    return s[s.find(start)+len(start):s.rfind(end)].strip()

def connectionMongoDb():
    # Connect to default mongo client on the localhost
    mongoClient = MongoClient()
    # Open the database named
    db = mongoClient['DungeonsAndDragons']
    return db

def createTheCollection(db):
    # Create the collection
    if db.get_collection("SpellCollection"):
        collection = db.get_collection("SpellCollection")
        db.drop_collection(collection)
    else:
        collection = db.create_collection("SpellCollection")
    return collection


def getTheCollection(db):
    # Get the data from collection from the database
    collection = db.get_collection("SpellCollection")
    return collection

def getDataFromTheCollection(collection):
    y = []
    for obj in collection.find():
        y.append(obj)
    return y

def insertTheWrappedData(collection, data):
    # Insert data in the collection
    collection.insert_many(data)



