import unittest
from groupby import groupby


class Test_groupby(unittest.TestCase):
    def test_if_groupby_works_right(self):
        function = lambda x: 'odd' if x % 2 else 'even'
        input = [1, 2, 3, 5, 8, 9, 10, 12]
        output = {'even': [2, 8, 10, 12], 'odd': [1, 3, 5, 9]}
        result = groupby(function, input)
        self.assertEqual(output, result)    


if __name__ == '__main__':
    unittest.main()
