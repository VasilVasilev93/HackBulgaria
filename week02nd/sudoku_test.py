import unittest
from sudoku import sudoku_solved


class Test_sudoku(unittest.TestCase):

    def test_if_one_of_rows_contains_2_or_more_same_digits(self):
        input = [
            [4, 5, 2, 3, 8, 9, 7, 1, 6],
            [3, 8, 7, 4, 6, 1, 2, 9, 5],
            [6, 1, 9, 2, 5, 7, 3, 4, 8],
            [9, 3, 5, 1, 2, 6, 8, 7, 4],
            [7, 6, 4, 9, 3, 8, 5, 2, 1],
            [1, 2, 8, 5, 7, 4, 6, 3, 9],
            [5, 7, 1, 8, 3, 2, 4, 6, 3],
            [8, 9, 6, 7, 4, 3, 1, 5, 2],
            [2, 4, 3, 6, 1, 5, 9, 8, 7]
        ]
        result = sudoku_solved(input)
        self.assertFalse(result)

    def test_if_one_of_columns_contains_2_or_more_same_digits(self):result = sudoku_solved(input)
        input = [
            [4, 5, 2, 3, 8, 9, 7, 1, 6],
            [3, 8, 7, 4, 6, 1, 2, 9, 5],
            [6, 1, 9, 2, 5, 7, 3, 4, 8],
            [1, 3, 5, 1, 2, 6, 8, 7, 4],
            [7, 6, 4, 9, 3, 8, 5, 2, 1],
            [1, 2, 8, 5, 7, 4, 6, 3, 9],
            [5, 7, 1, 8, 9, 2, 4, 6, 3],
            [8, 9, 6, 7, 4, 3, 1, 5, 2],
            [2, 4, 3, 6, 1, 5, 9, 8, 7]
        ]
        result = sudoku_solved(input)
        self.assertFalse(result)

    def test_if_one_of_submatrix_contains_2_or_more_same_digits(self):
        input = [
            [4, 5, 2, 3, 8, 9, 7, 1, 6],
            [3, 8, 7, 4, 6, 1, 2, 9, 5],
            [6, 1, 9, 2, 5, 7, 3, 4, 8],
            [9, 3, 5, 1, 2, 6, 8, 7, 4],
            [7, 6, 4, 9, 3, 8, 5, 2, 1],
            [1, 2, 8, 5, 7, 4, 6, 3, 9],
            [5, 7, 1, 8, 9, 2, 4, 6, 3],
            [8, 9, 6, 7, 4, 3, 3, 5, 2],
            [2, 4, 3, 6, 1, 5, 9, 8, 7]
        ]
        result = sudoku_solved(input)
        self.assertFalse(result)

    def test_if_none_of_rows_colums_and_submatrixes_contains_2_or_more_same_digits(self):
        input = [
            [4, 5, 2, 3, 8, 9, 7, 1, 6],
            [3, 8, 7, 4, 6, 1, 2, 9, 5],
            [6, 1, 9, 2, 5, 7, 3, 4, 8],
            [9, 3, 5, 1, 2, 6, 8, 7, 4],
            [7, 6, 4, 9, 3, 8, 5, 2, 1],
            [1, 2, 8, 5, 7, 4, 6, 3, 9],
            [5, 7, 1, 8, 9, 2, 4, 6, 3],
            [8, 9, 6, 7, 4, 3, 1, 5, 2],
            [2, 4, 3, 6, 1, 5, 9, 8, 7]
        ]
        result = sudoku_solved(input)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
