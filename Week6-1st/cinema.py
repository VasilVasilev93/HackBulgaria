from sqlalchemy.orm import Session
from movie import Movie
from reservation import Reservation
from projections import Projection
import create_base
import cinema_hall
from help_menu import help_menu
import ast


def add_movies(session):
    print("Adding movies to the database via the session object")
    session.add_all([
        Movie(name="The Hunger Games: Catching Fire", rating=7.9),
        Movie(name="Wreck-It Ralph", rating=7.8),
        Movie(name="Her", rating=8.3)])


def add_projections(session):
    print("Adding projections to the database via the session object")
    session.add_all([
        Projection(movieID=1, movie_type='3D', ptime="19:00", pdate="21.04"),
        Projection(movieID=2, movie_type='4DX', ptime="20:00", pdate="21.04"),
        Projection(movieID=3, movie_type='2D', ptime="18:00", pdate="21.04")])


def add_reservations(session):
    print("Adding reservations to the database via the session object")
    session.add_all([
        Reservation(username='Rado', projection_id=2, row=5, col=4),
        Reservation(username='Pesho', projection_id=1, row=5, col=4),
        Reservation(username='Goshko', projection_id=3, row=5, col=4)])


def print_query_result(query):
    for row in query:
        print (row)


def show_movies(session):
    all_movies = session.query(Movie).order_by(Movie.rating.desc()).all()
    print_query_result(all_movies)
    return all_movies


def show_projections(session, pID, pdate):
    if pdate is None:
        projections = session.query(Projection).filter(Movie.id == pID).filter(Movie.id == Projection.movieID).all()
    else:
        projections = session.query(Projection).\
            filter(Movie.id == pID).filter(Projection.pdate == pdate, Movie.id == Projection.movieID)\
            .order_by(Projection.pdate).all()
    print_query_result(projections)
    return projections


def fill_hall(hall, row, col):
    hall[row][col] = 'X'


def make_reservation(session):
    seats = []
    saved_seats = []
    name = input("Step 1 (User): Choose name>")
    tickets = int(input("Step 1 (User): Choose number of tickets>"))
    print ("Current movies:")
    show_movies(session)
    chosen_movie = input("Step 2 (Movie): Choose a movie>")
    movie = session.query(Movie).filter(Movie.id == chosen_movie).all()
    movie = movie[0]
    print ("Projections for {}:".format(movie))
    show_projections(session, chosen_movie, None)
    chosen_projection = input("Step 3 (Projection): Choose a projection>")
    taken_slots = session.query(Projection).filter(Projection.id == chosen_projection).count()
    slots_taken = session.query(Reservation.row, Reservation.col).\
        filter(Reservation.projection_id == chosen_projection).all()
    for slot in range(0, len(slots_taken)):
        row = slots_taken[slot][0]
        col = slots_taken[slot][1]
        cinema_hall.hall[row - 1][col - 1] = 'X'
    print (slots_taken)
    print("There are %s free slots in the hall." % (cinema_hall.free_slots - taken_slots))
    cinema_hall.print_hall()
    count = 1
    while tickets != 0:
        seat_chosen = ast.literal_eval(input("Step 4 (Seats): Choose seat((row, column)) %s>" % count))
        row = int(seat_chosen[0])
        col = int(seat_chosen[1])
        if cinema_hall.hall[row - 1][col - 1] == 'X':
            print ("This seat is already taken! Please choose different one.")
        elif row - 1 > cinema_hall.hall_rows or col - 1 > cinema_hall.hall_cols:
            print ("Please enter valid seat!")
        else:
            fill_hall(cinema_hall.hall, row - 1, col - 1)
            seats.append(seat_chosen)
            saved_seats.append(str(seat_chosen))
            count += 1
            tickets -= 1
    print("This is your reservation:")
    print("Movie: {}".format(movie))
    datetime = session.query(Projection.pdate, Projection.ptime).filter(Projection.id == chosen_projection).all()
    print("Date and Time: {} {} {}".format(datetime[0][0], datetime[0][1], movie))
    print("Seats: {}".format(','.join(saved_seats)))
    confirm = input("Step 5 (Confirm - type 'finalize') >")
    if confirm == 'finalize':
        for each in range(0, len(seats)):
            row = seats[each][0]
            col = seats[each][1]
            session.add(Reservation(username=name, projection_id=chosen_projection, row=row, col=col))
            session.commit()
        print ("Thanks")
    cinema_hall.hall = cinema_hall.reset_hall(cinema_hall.hall)


def main():
    create_base.Base.metadata.create_all(create_base.engine)
    session = Session(bind=create_base.engine)
    # add_movies(session)
    # add_projections(session)
    # add_reservations(session)
    session.commit()

    while True:
        command = input('>>> ').split()
        if command[0] == 'show-movies':
            show_movies(session)
        elif command[0] == 'show-projections':
            if len(command) == 3:
                show_projections(session, command[1], command[2])
            elif len(command) == 2:
                show_projections(session, command[1], None)
            else:
                print("Enter correct info.")
        elif command[0] == 'make-reservation':
            make_reservation(session)
        elif command[0] == 'cancel-reservation':
            pass
        elif command[0] == 'help':
            help_menu()
        elif command[0] == 'exit':
            break

if __name__ == '__main__':
    main()
