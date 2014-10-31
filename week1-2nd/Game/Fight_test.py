import unittest
from Fight import Fight
from hero import Hero
from orc import Orc
from weapon import Weapon


class Test_Fight(unittest.TestCase):
    def setUp(self):
        self.testOrc = Orc("TestOrc", 100, 1.4)
        self.testHero = Hero("TestHero", 100, "Tester")
        self.testOrc.weapon = Weapon("TestBrick", 30, 0.3)
        self.testHero.weapon = Weapon("TestOrcSlapper", 50, 0.6)
        self.testFight = Fight(self.testOrc, self.testHero)

    def test_simulate_fight(self):
        result = self.testFight.simulate_fight()
        self.assertIn(result, [self.testOrc, self.testHero])

    def test_simulate_fight_with_no_weapons_equipped(self):
        self.testOrc.weapon = None
        self.testHero.weapon = None
        result = self.testFight.simulate_fight()
        self.assertEqual(result, "No winner")

if __name__ == '__main__':
    unittest.main()
