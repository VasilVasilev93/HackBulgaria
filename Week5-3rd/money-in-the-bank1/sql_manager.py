import requests
import sqlite3
import smtplib
import hashlib
import getpass
from random import randint
from datetime import datetime, timedelta
from Client import Client

minimum_symbols = 8
maximum_fail_login = 5
fail_tries = 0

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    create_query = '''CREATE TABLE IF NOT EXISTS
        clients(id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                password TEXT,
                email TEXT UNIQUE,
                balance REAL DEFAULT 0,
                message TEXT)'''

    cursor.execute(create_query)


def create_sessions_table():
    create_sessions = '''CREATE TABLE IF NOT EXISTS
        sessions(id INTEGER REFERENCES clients(id),
                fail_tries INTEGER,
                block_expires TEXT)'''

    cursor.execute(create_sessions)


def change_message(new_message, logged_user):
    update_sql = '''UPDATE clients SET message = ? WHERE id = ?'''
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    correct = False
    while correct is False:
        if check_password_for_logged_user(logged_user, new_pass):
            update_sql = '''UPDATE clients SET password = ? WHERE id = ?'''
            cursor.execute(update_sql, (hash_password(new_pass), logged_user.get_id()))
            conn.commit()
            print("Password changed succesfully!")
            correct = True
        else:
            print("Enter valid password.")
            new_pass = getpass.getpass(prompt='Password: ')
            check_password_for_logged_user(logged_user, new_pass)


def __get_pass(filepath):
    f = open(filepath)
    password = f.read()
    f.close()
    return password


def get_user_password(username):
    user_pass_sql = ''' SELECT password FROM clients WHERE username = ? '''
    result = cursor.execute(user_pass_sql, (username,))
    for row in result:
        user_password = row
    user_password = user_password[0]
    return user_password


def send_email_with_new_password(email, new_password):
    password = __get_pass('secret')

    gmail_user = "vasilvasilev093@gmail.com"
    gmail_pwd = password
    FROM = 'vasilvasilev093@gmail.com'
    TO = [email]
    SUBJECT = "Your new password for T-bank"
    TEXT = "Enter this text to login in your account(without the brackets): '{}' ".format(new_password)

    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
            """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        #print ("Successfully sent the mail")
        return True
    except:
        print ("Failed to send mail(Email may not exist)")
        return False


def reset_password(username):
    printmsg = "Password reset succesfully! Check your mailbox and enter the received password: "
    if is_username_registered(username):
        email = get_email_of_user(username)
        password = generate_random_hash()
        change_password_sql = ''' UPDATE clients SET password = ? WHERE username = ? '''
        cursor.execute(change_password_sql, (password, username))
        conn.commit()
        send_email_with_new_password(email, password)
        new_password = getpass.getpass(prompt=printmsg)
        user_password = get_user_password(username)

        if str(new_password) == str(user_password):
            return special_login(username)

    else:
        print ("Such username does not exist!")
        return False


def containsSpecial(password):
    special_symbols = "!@#$%^&*()_+"
    for symbol in special_symbols:
        if symbol in password:
            return True
    return False


def check_password_length(password):
    if len(password) > minimum_symbols:
        return True
    print ("Your password must have more than %s symbols." % minimum_symbols)
    return False


def check_password_letters(password):
    if any(letter.islower() for letter in password) and any(letter.isupper() for letter in password):
        return True
    return False


def check_if_password_contains_username(username, password):
    if username not in password:
        return True
    return False


def check_if_password_contains_username_when_logged_in(logged_user, password):
    username = logged_user.get_username()
    if username not in password:
        return True
    return False


def check_password_for_logged_user(logged_user, password):
    return (containsSpecial(password) and check_password_length(password) and check_password_letters(password)
            and check_if_password_contains_username_when_logged_in(logged_user, password))


def check_password(username, password):
    return (containsSpecial(password) and check_password_length(password) and check_password_letters(password)
            and check_if_password_contains_username(username, password))


def is_email_used(email):
    email_sql = ''' SELECT email FROM clients '''
    result = cursor.execute(email_sql)
    for row in result:
        if row == email:
            return True
    False


def get_email_of_user(username):
    email_sql = ''' SELECT email FROM clients '''
    result = cursor.execute(email_sql)
    for row in result:
        email = row
    email = email[0]
    return email


def hash_password(password):
    password = password.encode('utf-8')
    password = (hashlib.sha1(password).hexdigest())

    return password


def generate_random_hash():
    random_number = randint(0, 100000)

    dk = hashlib.pbkdf2_hmac('sha1', b'password', b'salt', random_number)
    return hashlib.sha1(dk).hexdigest()


def register(username, password, email):
    correct = False
    while correct is False:
        if check_password(username, password) and not is_email_used(email):
            insert_sql = '''INSERT INTO clients (username, password, email) values (?, ?, ?)'''
            cursor.execute(insert_sql, (username, hash_password(password), email))
            conn.commit()
            get_userID_sql = ''' SELECT id FROM clients WHERE username = ?'''
            user = cursor.execute(get_userID_sql, (username,))
            user = user.fetchone()
            insert_into_sessions_sql = '''INSERT INTO sessions (id, fail_tries) values (?, ?)'''
            cursor.execute(insert_into_sessions_sql, (user[0], fail_tries))
            conn.commit()
            print("Registration Successfull")
            correct = True

        elif is_email_used(email):
            print("This email is already used for registration.")
            email = input("Enter other email: ")
        else:
            print("Enter valid password.")
            password = getpass.getpass(prompt='Password: ')
            check_password(username, password)


def is_username_registered(username):
    check_sql = ''' SELECT username FROM clients WHERE username = ?'''
    result = cursor.execute(check_sql, (username,))
    for row in result:
        return True
    return False


def get_id_of_username(username):
    get_id_sql = ''' SELECT id FROM clients WHERE username = ? '''
    result = cursor.execute(get_id_sql, (username,))
    for row in result:
        userID = row
    userID = userID[0]
    return userID


def add_fail_attempts(userID):
    fail_attepmts = get_fail_attempts(userID)
    fail_attepmts += 1
    add_sql = ''' UPDATE sessions SET fail_tries = ? WHERE id = ? '''
    cursor.execute(add_sql, (fail_attepmts, userID))
    conn.commit()


def get_fail_attempts(userID):
    get_fails_sql = ''' SELECT fail_tries FROM sessions WHERE id = ? '''
    result = cursor.execute(get_fails_sql, (userID,))
    for row in result:
        fail_attempts = row
    fail_attempts = fail_attempts[0]
    return fail_attempts


def reset_fail_attempts(userID):
    reset_fail_sql = ''' UPDATE sessions SET fail_tries = ? WHERE id = ? '''
    cursor.execute(reset_fail_sql, (fail_tries, userID))
    conn.commit()


def add_lockout(userID, time_of_lockout):
    add_lockout_sql = ''' UPDATE sessions SET block_expires = ? WHERE id = ? '''
    cursor.execute(add_lockout_sql, (time_of_lockout, userID))
    conn.commit()


def get_lockout(userID):
    get_lockout_sql = ''' SELECT block_expires FROM sessions WHERE id = ? '''
    result = cursor.execute(get_lockout_sql, (userID,))
    for row in result:
        lockout = row
    lockout = lockout[0]
    return lockout


def reset_lockout(userID):
    reset_lockout_sql = ''' UPDATE sessions SET block_expires = ? WHERE id = ? '''
    cursor.execute(reset_lockout_sql, (None, userID))
    conn.commit()


def bruteforce_protect(username):
    userID = get_id_of_username(username)
    add_fail_attempts(userID)
    fail_attempts = get_fail_attempts(userID)
    if fail_attempts >= maximum_fail_login:
        timeOfLastFailedLogin = datetime.now()
        lockOut = timeOfLastFailedLogin + timedelta(minutes=5)
        lockOut = format(lockOut, '%A %B - %H:%M:%S')
        add_lockout(userID, lockOut)
        reset_fail_attempts(userID)


def special_login(username):
    select_query = "SELECT id, username, balance, message FROM clients WHERE username = ? LIMIT 1"
    cursor.execute(select_query, (username,))
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False


def deposit(logged_user, balance):
    deposit_query = ''' UPDATE clients SET balance = ? WHERE id = ? '''
    cursor.execute(deposit_query, (balance, logged_user.get_id()))
    conn.commit()


def withdraw(logged_user, balance):
    withdraw_query = ''' UPDATE clients SET balance = ? WHERE id = ? '''
    cursor.execute(withdraw_query, (balance, logged_user.get_id()))
    conn.commit()


def get_tan(logged_user, tan_codes):
    codes_count = len(tan_codes)
    if codes_count > 0 and codes_count <= 10:
        print ("You have %s codes remaining." % codes_count)
        return False
    while (codes_count != 10):
        random_number = randint(0, 100000)

        hash1 = hashlib.pbkdf2_hmac('sha1', b'tan_code', b'salt', random_number)
        hash2 = hashlib.pbkdf2_hmac('sha1', b'tan_code', b'salt', random_number)
        tan_code = hashlib.sha1(hash1).hexdigest() + hashlib.sha1(hash2).hexdigest()
        tan_codes.append(tan_code)
    return tan_codes


def save_tan_codes(tan_codes):
    pass


def login(username, password):
    userID = get_id_of_username(username)
    lockout = str(get_lockout(userID))
    current_time = datetime.now()
    current_time = format(current_time, '%A %B - %H:%M:%S')
    if current_time > lockout:
        reset_lockout(userID)
        lockout = str(get_lockout(userID))
    if lockout == 'None':
        select_query = "SELECT id, username, balance, message FROM clients WHERE username = ? AND password = ? LIMIT 1"
        cursor.execute(select_query, (username, hash_password(password)))
        user = cursor.fetchone()

        if(user):
            return Client(user[0], user[1], user[2], user[3])
        else:
            return False
    elif lockout != 'None':
        print("You are blocked from login for till %s" % lockout)
        return False
    else:
        return False
