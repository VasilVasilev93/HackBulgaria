import unittest
from hero import Hero


class Test_hero(unittest.TestCase):

    def setUp(self):
        self.hero = Hero("Bron", 100, "DragonSlayer")

    def test_know_as_method(self):
        output = "Bron the DragonSlayer"
        result = self.hero.known_as()
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
