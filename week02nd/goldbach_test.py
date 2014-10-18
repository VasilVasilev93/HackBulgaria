import unittest
from goldbach import is_prime
from goldbach import goldbach


class Test_goldbach(unittest.TestCase):
    def test_if_check_prime_works_right(self):
        input = 0
        result = is_prime(input)
        self.assertFalse(result)
        input = 1
        result = is_prime(input)
        self.assertFalse(result)
        input = 2
        result = is_prime(input)
        self.assertTrue(result)
        input = 3
        result = is_prime(input)
        self.assertTrue(result)

    def test_if_goldbach_works_right(self):
        input = 10
        output = [(3, 7), (5, 5)]
        result = goldbach(input)
        self.assertEqual(output, result)

if __name__ == '__main__':
    unittest.main()
