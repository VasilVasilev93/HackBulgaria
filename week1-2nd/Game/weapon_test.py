import unittest
from weapon import Weapon


class Test_weapon(unittest.TestCase):
    def setUp(self):
        self.weapon = Weapon("Nutcracker", 20, 0.2)

    def test_weapon_type(self):
        output = "Nutcracker"
        result = self.weapon.type
        self.assertEqual(result, output)

    def test_critical_hit(self):
        results = []
        for hit in range(0, 1000):
            results.append(self.weapon.critical_hit())

        print (set(results))
        self.assertEqual(2, len(set(results)))

if __name__ == '__main__':
    unittest.main()
