import sqlite3


db = sqlite3.connect("cinema.db")
cursor = db.cursor()

cursor.execute(''' PRAGMA foreign_keys = ON ''')
db.commit()

cursor.execute(''' CREATE TABLE reservations(
                        id INTEGER PRIMARY KEY,
                        username TEXT,
                        projection_id INTEGER REFERENCES projections(id),
                        row INTEGER,
                        col INTEGER) ''')

db.commit()
