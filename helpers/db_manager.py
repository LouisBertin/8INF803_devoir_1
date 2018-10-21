import sqlite3
from pprint import pprint
import helpers.sorcerer as Sorcerer

connection = sqlite3.connect('tp1.db')
c = connection.cursor()

def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS sorcerer
    (
    casting_time VARCHAR(255),
    components VARCHAR(255),
    description VARCHAR(700),
    duration VARCHAR(255),
    effect VARCHAR(255),
    id INT PRIMARY KEY NOT NULL,
    level VARCHAR(255),
    range_value VARCHAR(255),
    school VARCHAR(255),
    spell_resistance VARCHAR(255),
    title VARCHAR(255)
    );''')
    connection.commit()

def insert_sorcerers(tab):
    c.execute('''DELETE FROM sorcerer''')
    c.executemany('''INSERT INTO sorcerer(
    casting_time, components, description, duration, effect, id, level, range_value, school, spell_resistance, title)
    VALUES (?,?,?,?,?,?,?,?,?,?,?)''',tab)
    connection.commit

def display_content():
    c.execute('''SELECT id, casting_time, components, duration FROM sorcerer''')
    all_rows = c.fetchall()
    for row in all_rows:
        print ('{0} : {1} - {2} - {3}'.format(row[0], row[1], row[2], row[3]))

def save_pito():
    c.execute('''SELECT id, title, components, level FROM sorcerer WHERE 
    sorcerer.components="V" 
    AND (level LIKE "%1%" OR level LIKE "%2%" OR level LIKE "%3%" OR level LIKE "%4%")''')
    all_rows = c.fetchall()
    for row in all_rows:
        print ('{0} : {1} - {2} - {3}'.format(row[0], row[1], row[2], row[3]))





