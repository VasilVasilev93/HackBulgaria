from Entity import Entity


class Hero(Entity):
    def __init__(self, name, health, nickname):
        super().__init__(name, health)
        self.nickname = nickname

    def known_as(self):
        return self.name + " the " + self.nickname

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
