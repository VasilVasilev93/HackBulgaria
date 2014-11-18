import sqlite3


db = sqlite3.connect("cinema.db")
cursor = db.cursor()

cursor.execute(''' CREATE TABLE projections(
                        id INTEGER PRIMARY KEY,
                        movie_id INTEGER REFERENCES movies(id),
                        type TEXT,
                        pdate DATE,
                        time TEXT) ''')

db.commit()

type1 = "3D"
pdate = "2014-04-01"
time = "20:00"
id_1 = 1

db.execute(''' INSERT INTO projections(movie_id, type, pdate, time) VALUES (?, ?, ?, ?) ''', (id_1, type1, pdate, time))
db.commit()
