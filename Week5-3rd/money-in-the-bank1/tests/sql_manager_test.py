import sys
import unittest

sys.path.append("..")

import sql_manager


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        sql_manager.create_clients_table()
        sql_manager.register('Tester', '$$$$Dim_4o')

    def tearDown(self):
        sql_manager.cursor.execute('DROP TABLE clients')

    def test_register(self):
        sql_manager.register('Dinko', '$$$$Dim_4o')

        sql_manager.cursor.execute(
            '''SELECT Count(*)  FROM clients WHERE username = ? AND password = ?''', ('Dinko', '$$$$Dim_4o'))
        users_count = sql_manager.cursor.fetchone()

        self.assertEqual(users_count[0], 1)

    def test_register_with_username_not_including_upper_lower_digit_special(self):
        sql_manager.register('Dinko', 'palachinkooooo!!!')

        sql_manager.cursor.execute(
            '''SELECT Count(*)  FROM clients WHERE username = ? AND password = ?''', ('Dinko', 'Dinko_23Lopatata$!!!'))
        users_count = sql_manager.cursor.fetchone()

        self.assertEqual(users_count[0], 0)

    def test_login(self):
        logged_user = sql_manager.login('Tester', '$$$$Dim_4o')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_login_with_sql_injection(self):
        logged_user = sql_manager.login("' OR 1 = 1 --", '123')
        print("YOU SHALL NOT PASS!!!")
        self.assertFalse(logged_user)

    def test_login_wrong_password(self):
        logged_user = sql_manager.login('Tester', '$$$$Dim_4o1')
        self.assertFalse(logged_user)

    def test_change_message(self):
        logged_user = sql_manager.login('Tester', '$$$$Dim_4o')
        new_message = "podaivinototam"
        sql_manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = sql_manager.login('Tester', '$$$$Dim_4o')
        new_password = "12345"
        sql_manager.change_pass(new_password, logged_user)

        logged_user_new_password = sql_manager.login('Tester', new_password)
        self.assertEqual(logged_user_new_password.get_username(), 'Tester')

if __name__ == '__main__':
    unittest.main()
