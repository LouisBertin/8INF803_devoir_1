from pprint import pprint
import sqlite3
import helpers.db_manager as DBmanager
import helpers.sorcerer as Sorcerer
import helpers.mapReduce as MapReduce
import helpers.tools as Tools


# Connect to the database
db = Tools.connectionMongoDb()

option = True
while option:
    print("""   1. Wrap Dungeons and dragons spells\n   2. MapReduce the data in MongoDb\n   3. Use sqlite to save Pito\n   Other option quit the program""")
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
        # Reduce data
        reduced = MapReduce._reduce(mapped)
        # Write data in a file
        with open('data.txt', 'w') as f:
            for item in reduced:
                f.write("%s\n" % item)
        f.close()
        # Print data
        print("\n Spells which can be used by Pitto to save himself")
        for spell in reduced:
            pprint(spell['title'])
        print("\n The spell List (with more info) is stored in the projet folder, it's named data.txt \n\n")
    elif option =="3":
        #Connect DB
        #connection = sqlite3.connect('tp1.db')
        #c = connection.cursor()
        #Create table
        print("\nProcessing ...\n")
        tab=Sorcerer.get_all(1,1976)
        DBmanager.create_table()
        #Insert each sorcerer
        DBmanager.insert_sorcerers(tab)
        #Find sorcerer to save Pito
        print("\n These are the sorcerer spells that can save Pito : \n")
        DBmanager.save_pito();
        print ("\n\n")
    else:
        option = False
        print("\n Bye, see you soon!")



