import unittest
from ab import is_an_bn


class Test_ab(unittest.TestCase):

    def test_if_word_has_equal_and_consecutive_a_and_b(self):
        result = is_an_bn("aaabbb")
        self.assertTrue(result)

    def test_if__word_is_not_empty(self):
        word = ("bbbaaa")
        self.assertTrue(word)

if __name__ == '__main__':
    unittest.main()
