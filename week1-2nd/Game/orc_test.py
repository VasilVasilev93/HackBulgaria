import unittest
from orc import Orc


class Test_orc(unittest.TestCase):
    def setUp(self):
        self.orc = Orc("Feqta Na Zybkite", 100, 2.0)

    def test_orc_berserk(self):
        self.assertEqual(2.0, self.orc.berserk_factor)

if __name__ == '__main__':
    unittest.main()
