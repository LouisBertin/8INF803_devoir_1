from pprint import pprint
import helpers.sorcerer as Sorcerer
import helpers.mapReduce as MapReduce
import helpers.tools as Tools


# Connect to the database
db = Tools.connectionMongoDb()

option = True
while option:
    print("""   1. Wrap Dungeons and dragons spells in MongoDb\n   2. MapReduce the data in MongoDb\n   Other option quit the program""")
    option = input("\n   What would you like to do? ")
    if option == "1":
        # Max number spell is 1976 (change to test as you wish)
        data = Sorcerer.get_all_sorcerer(1, 1976)
        # Create the collection if no exist
        collection = Tools.createTheCollection(db)
        # Store the data in the collection
        Tools.insertTheWrappedData(collection, data)
        print("\n Wrapped data store in database")

    elif option == "2":
        # Get the collection which contain the data from the wrapper
        collection = Tools.getTheCollection(db)
        # Get the data from the mongoDb collection
        spells = Tools.getDataFromTheCollection(collection)
        # Map data
        mapped = MapReduce._map(spells)
        # Filter data
        filtered = MapReduce._filter(mapped)
        # Write data in a file
        with open('data.txt', 'w') as f:
            for item in filtered:
                f.write("%s\n" % item)
        f.close()
        # Print data
        print("\n Spells which can be use by Pitto to save himself")
        for spell in filtered:
            pprint(spell['title'])
        print("\n The spell List (with more info) is stored in the projet folder, it's named data.txt \n\n")
    else:
        print("\n Don't know what you mean, try again")



