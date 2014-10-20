import unittest
from uniquewords import unique_words_count


class Test_uniqewords(unittest.TestCase):

    def test_if_words_are_unique(self):
        input = ["python", "apple", "ruby"]
        output = 3
        result = unique_words_count(input)
        self.assertEqual(output, result)

    def test_if_words_are_not_unique(self):
        input = ["python", "python", "python", "ruby", "ruby"]
        output = 2
        result = unique_words_count(input)
        self.assertEqual(output, result)

    def test_if_words_are_or_arenot_unique(self):
        input = ["python", "python", "python", "ruby"]
        output = 2
        result = unique_words_count(input)
        self.assertEqual(output, result)

    def test_if_given_array_is_empty(self):
        input = []
        output = 0
        result = unique_words_count(input)
        self.assertEqual(output, result)

if __name__ == '__main__':
    unittest.main()
