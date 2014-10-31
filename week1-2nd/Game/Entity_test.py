import unittest
from Entity import Entity
from weapon import Weapon


class Test_Entity(unittest.TestCase):

    def setUp(self):
        self.entity = Entity("Kung-Fu Balhar", 100)
        self.otherentity = Entity("Balha", 100)
        self.entity.weapon = Weapon("Kaish", 50, 0.5)

    def test_entity_name(self):
        output = "Kung-Fu Balhar"
        result = self.entity.name
        self.assertEqual(result, output)

    def test_get_entity_health(self):
        output = 100
        result = self.entity.get_health()
        self.assertEqual(result, output)

    def test_is_entity_alive(self):
        self.assertTrue(self.entity.is_alive())

    def test_entity_take_damage(self):
        health_left = 60
        damage = 40
        result = self.entity.get_health() - damage
        self.assertEqual(health_left, result)

    def test_entity_take_healing_when_not_dead_and_has_max_hp(self):
        self.assertFalse(self.entity.take_healing(10))

    def test_entity_take_healing_when_not_dead_and_has_less_than_max_hp(self):
        self.entity.health -= 10
        self.assertTrue(self.entity.take_healing(10))

    def test_entity_take_healing_when__dead(self):
        self.entity.health -= 100
        self.assertFalse(self.entity.take_healing(10))

    def test_has_weapon_when_weapon_not_equipped(self):
        result = self.otherentity.has_weapon()
        self.assertFalse(result)

    def test_has_weapon_when_weapon_equipped(self):
        self.weapon = Weapon("Mighty Axe", 25, 0.2)
        self.entity.equip_weapon(self.weapon)
        result = self.entity.has_weapon()
        self.assertTrue(result)

    def test_equip_weapon(self):
        self.weapon = Weapon("Mighty Axe", 25, 0.2)
        result = self.entity.equip_weapon(self.weapon)
        self.assertTrue(result)

    def test_damage_of_entity_when_weapon_equipped(self):
        self.assertEqual(self.entity.attack(), 50)

    def test_damage_of_entity_when_weapon_not_equipped(self):
        self.assertEqual(self.otherentity.attack(), 0)

if __name__ == '__main__':
    unittest.main()
