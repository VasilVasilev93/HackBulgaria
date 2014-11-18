import sqlite3

db = sqlite3.connect("cinema.db")
cursor = db.connect()


def insertMovie():
    name = input("name>")
    rating = input("rating>")
    cursor.execute(''' INSERT INTO movies(name, rating) VALUES(?, ?)''', name, rating)
    db.commit()


def listMovies():
    print ("All movies on screen: ")
    cursor.execute(''' SELECT movies(name) from movies ''')
    db.commit()


def removeMovie():
    print("Choose a movie to remove: ")
    listMovies()
    movieIndex = input("Enter the movie's index you want to remove")
    cursor.execute(''' DELETE FROM moives where movie(id) = ? ''', (movieIndex,))
    db.commit()


def rateMovie():
    pass
