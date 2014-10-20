import unittest
from spameggs import prepare_meal


class Test_spameggs(unittest.TestCase):
    def test_if_given_int_is_0(self):
        input = 0
        output = "eggs"
        result = prepare_meal(input)
        self.assertEqual(result, output)

    def test_if_given_int_is_not_divisible_by_3_or_5(self):
        input = 4
        output = ""
        result = prepare_meal(input)
        self.assertEqual(result, output)

    def test_if_given_int_is_divisible_by_3_but_not_5(self):
        input = 9
        output = "spam spam "
        result = prepare_meal(input)
        self.assertEqual(result, output)

    def test_if_given_int_is_divisible_by_5_but_not_3(self):
        input = 10
        output = "eggs"
        result = prepare_meal(input)
        self.assertEqual(result, output)

    def test_if_given_int_is_divisible_by_5_and_3_and_higher_than_10(self):
        input = 540
        output = "spam spam spam and eggs"
        result = prepare_meal(input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
