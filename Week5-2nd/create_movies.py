import sqlite3
from cinema import Cinema


db = sqlite3.connect("cinema.db")
cursor = db.cursor()
cursor.execute('''CREATE TABLE movies(
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    rating REAL)''')

db.commit()


name1 = "Star Wars 7"
rating1 = 10.00

db.execute(''' INSERT INTO movies(name, rating) VALUES (?, ?) ''', (name1, rating1))
db.commit()
