class Entity():

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon = None

    def get_health(self):
        return self.health

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def take_damage(self, damage_points):
        if self.health < damage_points:
            self.health = 0
        else:
            self.health -= damage_points

    def take_healing(self, healing_points):
        if self.is_alive() and self.health < 100:
            self.health += healing_points
            return True
        return False

    def has_weapon(self):
        if self.weapon is not None:
            return True
        return False

    def equip_weapon(self, weapon):
        self.weapon = weapon
        return True

    def attack(self):
        if self.weapon is None:
            return 0
        else:
            return self.weapon.damage
