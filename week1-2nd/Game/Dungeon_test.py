import unittest
from Dungeon import Dungeon
from hero import Hero
from orc import Orc
import os


class Test_Dungeon(unittest.TestCase):

    def setUp(self):
        self.filename = "map"
        self.contents = """S.##......
#.##..###.
#.###.###.
#.....###.
###.#####S"""

        with open(self.filename, "w+") as f:
            f.write(self.contents)
        f.close()
        self.testDungeon = Dungeon("map")
        self.orc = Orc("TestOrc", 100, 1.3)
        self.hero = Hero("TestHero", 100, "Teter")

    def tearDown(self):
        self.testDungeon.spawnlist.clear()
        del self.testDungeon.spawnedplayers[:]
        os.remove(self.filename)

    def test_init(self):
        with open(self.filename, "r+") as f:
            result = f.read()
        f.close()
        self.assertEqual(self.contents, result)

    def test_print_map(self):
        output = self.testDungeon.print_map()
        with open(self.filename, "r") as f:
            result = f.read()
        f.close()
        self.assertEqual(output, result)

    def test_spawn_character(self):
        self.testDungeon.spawn("TestOrc", self.orc)
        self.testDungeon.spawnlist = {"TestOrc": self.orc}
        self.testDungeon.spawnedplayers.append("TestOrc")
        with open(self.filename, "r+") as f:
            actual = f.read()
            f.close()
        contents = """O.##......
#.##..###.
#.###.###.
#.....###.
###.#####S"""
        self.assertEqual(actual, contents)

    def test_spawn_already_spawned_character(self):
        self.testDungeon.spawnlist = {"TestOrc": self.orc}
        self.testDungeon.spawnedplayers.append("TestOrc")
        result = self.testDungeon.spawn("TestOrc", self.orc)
        self.assertEqual("Character is already spawned.", result)

    def test_spawn_with_no_free_slots(self):
        self.filename = "map"
        self.contents = """..##......
#.##..###.
#.###.###.
#.....###.
###.#####."""
        with open(self.filename, "w+") as f:
            f.write(self.contents)
            f.close()
        result = self.testDungeon.spawn("TestOrc1", self.orc)
        self.assertEqual("No free spawn slot.", result)

    def test_spawn_all_free_slots(self):
        self.testDungeon.spawn("TestHero", self.hero)
        self.testDungeon.spawn("TestOrc", self.orc)
        self.testDungeon.spawnlist = {"TestHero": self.hero}
        self.testDungeon.spawnlist = {"TestOrc": self.orc}
        self.testDungeon.spawnedplayers.append("TestHero")
        self.testDungeon.spawnedplayers.append("TestOrc")
        with open(self.filename, 'r+') as f:
            actual = f.read()
            f.close()
        self.contents = """H.##......
#.##..###.
#.###.###.
#.....###.
###.#####O"""
        self.assertEqual(actual, self.contents)

#     def test_move_character(self):
#         self.testDungeon.spawnlist = {"TestHero": self.hero}
#         self.testDungeon.spawnlist = {"TestOrc": self.Orc}
#         self.testDungeon.spawnedplayers.append("TestHero")
#         self.testDungeon.spawnedplayers.append("TestOrc")
#         self.testDungeon.spawn("TestHero", self.hero)
#         self.testDungeon.spawn("TestOrc", self.orc)
#         result = self.testDungeon.move("TestHero", "right")
#         print ("HERE IS THE MAP")
#         self.testDungeon.print_map()
#         self.assertTrue(result)

#     def test_move_hero_to_free_slot(self):
#         self.testDungeon.spawn("TestHero", self.hero)
#         self.testDungeon.spawn("TestOrc", self.orc)
#         result = self.testDungeon.move("Hero", "right")
#         self.contents = """.H##......
# #.##..###.
# #.###.###.
# #.....###.
# ###.#####O"""
#         self.assertEqual(result, self.contents)

#     def test_move_orc_to_free_slot(self):
#         self.testDungeon.spawn("TestHero", self.hero)
#         self.testDungeon.spawn("TestOrc", self.orc)
#         result = self.testDungeon.move("Orc", "up")
#         self.contents = """H.##......
# #.##..###.
# #.###.###.
# #.....###O
# ###.#####."""
#         self.assertEqual(result, self.contents)

    # def test_get_player_position(self):
    #     self.testDungeon.spawn("TestHero", self.hero)
    #     self.testDungeon.spawn("TestOrc", self.orc)
    #     result = self.testDungeon.get_player_position("TestOrc")
    #     self.testDungeon.print_map()
    #     self.assertEqual(result, 53)


if __name__ == '__main__':
    unittest.main()
