import sqlite3
from pprint import pprint
import helpers.sorcerer as Sorcerer

connection = sqlite3.connect('tp1.db')
c = connection.cursor()

def create_db():
    c.execute('''CREATE TABLE sorcerer
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
    c.executemany('''INSERT INTO sorcerer(
    casting_time, components, description, duration, effect, id, level, range_value, school, spell_resistance, title)
    VALUES (?,?,?,?,?,?,?,?,?,?,?)''',tab)
    connection.commit


#DEMO

create_db()
data=Sorcerer.get_all(1,8)
pprint(data)
data1 = [("a", "a", "a", "a", 1, "a", "a", "a", "a", "a"),
         ("b", "b", "b", "b", 2, "b", "b", "b", "b", "b"),
         ("c", "c", "c", "c", 3, "c", "c", "c", "c", "c")]
pprint(data1)
insert_sorcerers(data)
c.execute('''SELECT casting_time, components, duration FROM sorcerer''')
allrows = c.fetchall()
for row in allrows:
    print('{0} / {1} / {2}'.format(row[0], row[1], row[2]))


