import unittest
from fibonaccilists import nth_fib_lists


class Test_fibonnacilists(unittest.TestCase):

    def test_if_fib_number_is_1st(self):
        listA = [1, 2]
        listB = [1, 3]
        input = 1
        output = [1, 2]
        result = nth_fib_lists(listA, listB, input)
        self.assertEqual(output, result)

    def test_if_given_lists_are_not_empty(self):
        listA = [1]
        listB = [2]
        self.assertNotEqual([], listA)
        self.assertNotEqual([], listB)

    def test_if_input_is_not_empty(self):
        input = 1
        self.assertNotEqual(0, input)

if __name__ == '__main__':
    unittest.main()
