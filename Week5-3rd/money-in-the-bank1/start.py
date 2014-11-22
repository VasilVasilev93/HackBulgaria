import sql_manager
import getpass


def main_menu():
    print("Welcome to our bank service. You are not logged in. \nPlease register or login")

    while True:
        command = input("$$$>").split(' ')

        if command[0] == 'register':
            username = input("Enter your username: ")
            email = input("Enter your email: ")
            password = getpass.getpass(prompt='Password: ')

            sql_manager.register(username, password, email)

        elif command[0] == 'login':
            username = input("Enter your username: ")
            password = getpass.getpass(prompt='Password: ')

            if sql_manager.is_username_registered(username):
                logged_user = sql_manager.login(username, password)
                if logged_user:
                    logged_menu(logged_user)

                elif sql_manager.is_username_registered(username):
                    sql_manager.bruteforce_protect(username)
                    print("Incorrect username/password")

            else:
                print("Login failed")

        elif command[0] == 'send-reset-password':
            username = command[1]
            logged_user = sql_manager.reset_password(username)
            if logged_user:
                logged_menu(logged_user)
        elif command[0] == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("send-reset-password [username] - for resetting password!")
            print("exit - for closing program!")

        elif command[0] == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            new_pass = getpass.getpass(prompt='Password: ')
            sql_manager.change_pass(new_pass, logged_user)

        elif command == 'deposit':
            amount = input("Enter amount: ")
            if logged_user.deposit(float(amount)):
                new_balance = logged_user.get_balance()
                sql_manager.deposit(logged_user, new_balance)

        elif command == 'test':
            sql_manager.test_func(logged_user)

        elif command == 'withdraw':
            amount = input("Enter amount: ")
            if logged_user.withdraw(float(amount)):
                new_balance = logged_user.get_balance()
                sql_manager.withdraw(logged_user, new_balance)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'logout':
            print("Goodbye %s!" % logged_user.get_username())
            break

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")


def main():
    sql_manager.create_clients_table()
    sql_manager.create_sessions_table()
    main_menu()

if __name__ == '__main__':
    main()
