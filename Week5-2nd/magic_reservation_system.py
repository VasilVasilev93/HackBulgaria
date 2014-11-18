import sqlite3


hall = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]


def reset_hall():
    hall = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]


def free_slots():
    count = 0
    for row in hall:
        for slot in row:
            count += 1
    return count


db = sqlite3.connect('cinema.db')
db.row_factory = sqlite3.Row
cursor = db.cursor()


def show_movies():
    print ("Current Movies: ")
    result = cursor.execute(''' SELECT * FROM movies ORDER BY movies.rating''')
    for row in result:
        print ('[{}] - {} ({})'.format(row["id"], row["name"], row["rating"]))


def show_free_slots_for_movies(movie):
    print ("Projections for movie '{}': ".format(movie))
    result = cursor.execute(''' SELECT *, type FROM movies, projections
                                where movies.name = ? ORDER BY movies.rating''', (movie,))
    for row in result:
        print ('[{}] - {} {} ({}) - {} spots available'.format(row["id"], row["pdate"], row["ptime"], free_slots()))


def show_movie_projections(id_movie, date):
    if date == "":
        result = cursor.execute(''' SELECT * FROM projections inner join movies
                                    on projections.movie_id = movies.id
                                    WHERE movie_id = ? ''', (id_movie))
    else:
        result = cursor.execute(''' SELECT * FROM projections inner join movies
                                    on projections.movie_id = movies.id
                                    WHERE movie_id = ?
                                    AND pdate = ?
                                    ORDER BY pdate ''', (id_movie, date))
    count = 0
    for row in result:
        if count == 0:
            print ("Projections for movie '{}': ".format(row["name"]))
            count += 1
        print ('[{}] - {} {} - ({})'.format(row["movie_id"], row["pdate"], row["time"], row["type"]))


def make_reservation():
    name = input("Step 1(User): Choose name>")
    number_of_tickets = input("Step 1 (User): Choose number of tickets>")
    show_movies()
    movie_choice = input("Step 2 (Movie): Choose a movie>")
    show_free_slots_for_movies(movie_choice)
    projection_choice = input("Step 3 (Projection): Choose a projection>")


def cancel_reservation(name):
    pass


def exit():
    pass


def help():
    pass


def main():
    exit = False

    while (exit is False):
        command = input("command>").split(' ')
        if command[0] == 'show_projections':
            show_movie_projections(command[1], command[2])
        elif command[0] == 'reserve':
            make_reservation()
        elif command[0] == 'cansel_reservation':
            delete_employee(command[1])
        elif command[0] == 'exit':
            add_employee()
        elif command[0] == 'help':
            update_employee(command[1])
        else:
            print("Enter valid command")

if __name__ == "__main__":
    main()
