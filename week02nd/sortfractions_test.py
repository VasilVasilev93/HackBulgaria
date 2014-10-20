import unittest
from sortfractions import sort_fractions


class Test_sortfractions(unittest.TestCase):

    def test_if_sorting_of_fractions_works_right(self):
        input = [(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]
        output = [(11, 39), (15, 32), (5, 6), (7, 8), (3, 2), (22, 7)]
        result = sort_fractions(input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
