from sqlalchemy.orm import Session
from sqlalchemy import update
from create_base import Base, engine
from random import randint
from high_scores import HighScores
from player import Player


min_num = 1
max_num = 10
min_operation = 1
max_operation = 4


def generate_operation(choice):
    if choice == 1:
        return 'x'
    elif choice == 2:
        return '+'
    elif choice == 3:
        return '-'
    elif choice == 4:
        return '^'


def is_username_registered(session, username):
    users = []
    result = session.query(HighScores.player_name).all()
    for record in result:
        users.append(record[0])
        try:
            if record[1]:
                users.append(record[1])
        except IndexError:
            pass
    if username in users:
        return True
    else:
        return False


def generate_numbers():
    first_num = randint(min_num, max_num)
    second_num = randint(min_num, max_num)
    return (first_num, second_num)


def start_game(session):
    counter = 1
    name = input("Enter your playername>")
    if is_username_registered(session, name):
        player = Player(name)
        print ("Welcome back, %s" % name)
    else:
        player = Player(name)
        add_record(session, player)

    while True:
        first_number, second_number = generate_numbers()
        operation = generate_operation(randint(min_operation, max_operation))
        print("Question #%s" % counter)
        print("What is the answer to %s %s %s?" % (first_number, operation, second_number))
        answer = int(input("?>"))
        if answer == calculate(first_number, second_number, operation):
            print("Correct!")
            player._add_points(counter)
            print(player._get_points())
            add_points_to_player(session, player)
        else:
            print("Incorrect answer! Ending game. Your score is: %s" % player._get_points())
            return False
        counter += 1


def calculate(first_number, second_number, operation):
    if operation == 'x':
        print (first_number*second_number)
        return first_number*second_number
    elif operation == '+':
        print (first_number+second_number)
        return first_number + second_number
    elif operation == '-':
        print (first_number-second_number)
        return first_number - second_number
    elif operation == '^':
        print (first_number**second_number)
        return first_number**second_number


def print_query_result(query):
    for row in query:
        print (row)


def add_record(session, player):
    session.add(HighScores(player_name=player.name, points=player._get_points()))
    session.commit()


def add_points_to_player(session, player):
    session.execute(update(HighScores).where(HighScores.player_name == player.name).values(points=player._get_points()))
    session.commit()


def show_high_scores(session):
    query = session.query(HighScores).order_by(HighScores.points.desc()).all()
    print_query_result(query)
    return query


def main():
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    session.commit()
    print('Welcome to the "Do you even math?" game!\n\
        Here are yoyr options:\n\
        - start\n\
        - highscores')
    while True:
        command = input("?>")

        if command == 'start':
            start_game(session)
        elif command == 'highscores':
            show_high_scores(session)
        elif command == 'exit':
            break

if __name__ == '__main__':
    main()
