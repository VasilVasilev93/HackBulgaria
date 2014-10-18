import unittest
from memberoffiblist import member_of_nth_fib_lists


class Test_memberoffiblist(unittest.TestCase):
    def test_if_fib_number_is_1st(self):
        listA = [1, 2]
        listB = [1, 3]
        input = [1, 2]
        result = member_of_nth_fib_lists(listA, listB, input)
        self.assertTrue(result)

    def test_if_fib_number_is_2nd(self):
        listA = [1, 2]
        listB = [1, 3]
        input = [1, 3]
        result = member_of_nth_fib_lists(listA, listB, input)
        self.assertTrue(result)

    def test_if_fib_number_is_3rd(self):
        listA = [1, 2]
        listB = [1, 3]
        input = [1, 2, 1, 3]
        result = member_of_nth_fib_lists(listA, listB, input)
        self.assertTrue(result)

    def test_if_input_is_empty(self):
        listA = [1, 2]
        listB = [1, 3]
        input = [0]
        result = member_of_nth_fib_lists(listA, listB, input)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
