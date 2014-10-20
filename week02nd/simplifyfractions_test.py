import unittest
from simplifyfractions import simplify_fraction


class Test_simplifyfractions(unittest.TestCase):
    def test_if_given_arguments_are_0(self):
        input = (0, 0)
        output = (0, 0)
        result = simplify_fraction(input)
        self.assertEqual(result, output)

    def test_if_given_arguments_are_prime(self):
        input = (56, 67)
        output = (56, 67)
        result = simplify_fraction(input)
        self.assertEqual(result, output)

    def test_if_given_arguments_are_not_prime(self):
        input = (16, 8)
        output = (2, 1)
        result = simplify_fraction(input)
        self.assertEqual(result, output)

    def test_if_given_arguments_are_not_prime_but_not_simplifiable(self):
        input = (15, 62)
        output = (15, 62)
        result = simplify_fraction(input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
