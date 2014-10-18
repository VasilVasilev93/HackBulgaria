import unittest
from countwords import count_words


class Test_countwords(unittest.TestCase):

    def test_if_words_are_unique(self):
        input = ["python", "apple", "ruby"]
        output = {'python': 1, 'apple': 1, 'ruby': 1}
        result = count_words(input)
        self.assertEqual(output, result)

    def test_if_words_are_not_unique(self):
        input = ["python", "python", "python", "ruby"]
        output = {'python': 3, 'ruby': 1}
        result = count_words(input)
        self.assertEqual(output, result)

if __name__ == '__main__':
    unittest.main()
