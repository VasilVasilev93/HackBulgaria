import unittest
from magicsq import magic_square


class Test_magicsq(unittest.TestCase):
    def test_if_magicsq_calculates_right(self):
        input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = magic_square(input)
        self.assertFalse(result)

        input = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
        result = magic_square(input)
        self.assertTrue(result)

        input = [[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]
        result = magic_square(input)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
