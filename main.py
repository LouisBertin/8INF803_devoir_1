from pprint import pprint
import sqlite3
import helpers.sorcerer as Sorcerer
import helpers.db_manager as DBmanager

# QUESTION 1
data = Sorcerer.get_all_sorcerer(1, 7)
pprint(data)


# QUESTION 3
connection = sqlite3.connect('tp1.db')
c = connection.cursor()
DBmanager.create_db()
DBmanager.insert_sorcerers(Sorcerer.get_all(1,7))
DBmanager.display_content()




