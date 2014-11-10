import sqlite3

result = ""

conn = sqlite3.connect('company.db')
conn.row_factory = sqlite3.Row

cursor = conn.cursor()


def list_employees():
    result = cursor.execute('''SELECT name, position from company''')
    for row in result:
        print ('{} - {}'.format(row["name"], row["position"]))


def monthly_spending():
    result = cursor.execute('''SELECT sum(monthly_salary) from company''')
    monthly = result.fetchone()
    print ("The company is spending ${} every month!".format(monthly[0]))


def add_employee():
    name = input("name>")
    monthly_salary = input("monthly_salary>")
    yearly_bonus = input("yearly_bonus>")
    position = input("position>")

    cursor.execute(''' INSERT INTO company(name, monthly_salary, yearly_bonus, position) VALUES(?, ?, ?, ?)''',
                   (name, monthly_salary, yearly_bonus, position))
    conn.commit()


def delete_employee(employee_id):
    cursor.execute('''DELETE FROM company WHERE id = ? ''', (employee_id,))
    conn.commit()


def __parse_update_query(values):
    query = 'UPDATE company SET '
    for value in values:
        query += '{0} = ?, '.format(value)
    return query[:-2] + ';'


def update_employee(employee_id):
    name = input("name>")
    monthly_salary = input("monthly_salary>")
    yearly_bonus = input("yearly_bonus>")
    position = input("position>")

    query = 'UPDATE company SET name = ?, monthly_salary = ?, yearly_bonus = ?, position = ? WHERE id = ?;'
    cursor.execute(query, (name, monthly_salary, yearly_bonus, position, employee_id))
    conn.commit()


def main():
    exit = False

    while (exit is False):
        command = input("command>").split(' ')
        if command[0] == 'list_employees':
            list_employees()
        elif command[0] == 'monthly_spending':
            monthly_spending()
        elif command[0] == 'delete':
            delete_employee(command[1])
        elif command[0] == 'add':
            add_employee()
        elif command[0] == 'update':
            update_employee(command[1])
        elif command[0] == "exit":
            exit = True
        else:
            print("Enter valid command")

if __name__ == "__main__":
    main()
