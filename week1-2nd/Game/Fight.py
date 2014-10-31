from random import randint


class Fight():
    def __init__(self, Hero, Orc):
        self.Hero = Hero
        self.Orc = Orc

    def get_starting_character(self):
        coin = randint(0, 100)
        if coin < 50:
            return (self.Hero, self.Orc)
        return (self.Orc, self.Hero)

    def simulate_fight(self):
        if self.Hero.weapon is None and self.Orc.weapon is None:
            return "No winner"

        (attacker, deffender) = self.get_starting_character()

        while self.Hero.is_alive() and self.Orc.is_alive():
            damage = self.attacker.attack()
            deffender.take_damage(damage)
            attacker, deffender = deffender, attacker

        if self.Orc.is_alive():
            return self.Orc
        return self.Hero
