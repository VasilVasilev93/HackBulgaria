from hero import Hero
from orc import Orc
from Fight import Fight
from weapon import Weapon
from random import randint


entities = []
weapons = None


class Dungeon():
    spawnlist = {}
    spawnedplayers = []
    weapons = {}

    def __init__(self, filepath):
        self.filepath = filepath

    def reinitialize_file(self, filepath, new_content):
        f = open(filepath, "w+")
        f.write("".join(new_content))
        f.close()

    def print_map(self):
        f = open(self.filepath, "r+")
        map = f.read()
        f.close
        print(map)
        return map

    def get_opposite_player_indicator(self, player):
        if isinstance(player, Orc):
            return "H"
        if isinstance(player, Hero):
            return "O"

    def get_player_indicator(self, player):
        if isinstance(player, Orc):
            return "O"
        if isinstance(player, Hero):
            return "H"

    def get_player_position(self, player):
        count = 0
        current_entity_count = 0
        player_count = -1
        player_entity = self.spawnlist[player]
        for item in self.spawnlist:
            if self.spawnlist[item] == player_entity:
                current_entity_count += 1
            if current_entity_count > 1:
                p_index = self.spawnedplayers.index(player)
            else:
                p_index = 0
        player_type = self.get_player_indicator(player_entity)
        with open(self.filepath, 'r') as f:
            for line in f:
                for alpha in line:
                    if alpha == player_type:
                        player_count += 1
                        if player_count == p_index:
                            pos = f.seek(count)
                            return pos
                            break
                    count += 1

    def spawn(self, player_name, entity):
        global entities
        #entities = []
        entities.append(entity)
        if player_name in self.spawnlist:
            return "Character is already spawned."
        else:
            output = []
            f = open(self.filepath, "r+")
            output += f.read()
            f.close()
            if "S" in "".join(output):
                for n, i in enumerate(output):
                    if i == 'S':
                        self.spawnlist[player_name] = entity
                        self.spawnedplayers.append(player_name)
                        output[n] = self.get_player_indicator(entity)
                        break
            else:
                return "No free spawn slot."
            f = open(self.filepath, "w+")
            f.write("".join(output))
            f.close()

    def move(self, player, direction):

        real_player = self.spawnlist[player]
        pos = self.get_player_position(player)
        output = []
        player_indicator = self.get_player_indicator(self.spawnlist[player])
        opposite_player_indicator = self.get_opposite_player_indicator(
            self.spawnlist[player])
        f = open(self.filepath, "r")
        for line in f:
            line_len = len(line) - 1
            break
        f = open(self.filepath, "r+")
        output += f.read()
        f.close()
        if player_indicator in "".join(output):
            for n, i in enumerate(output):
                if i == player_indicator and i != '\n':
                    if direction == "up" and output[pos - line_len - 1] != '#':
                        if opposite_player_indicator == output[pos - line_len - 1]:
                            enemy_index = (self.choose_enemy(
                                output, player_indicator,
                                opposite_player_indicator, output[pos - line_len - 1]))
                            enemy = self.spawnlist[
                                self.spawnedplayers[enemy_index]]
                            enemyname = self.spawnedplayers[enemy_index]
                            self.fight(output, real_player, enemy, player, enemyname, pos,
                                       pos - line_len - 1, player_indicator,
                                       self.filepath)
                        else:
                            output[pos] = '.'
                            output[pos - 1] = player_indicator
                            self.reinitialize_file(self.filepath, output)

                    elif (direction == "down" and
                          output[pos + line_len + 1] != '#'):
                        if opposite_player_indicator == output[pos + line_len + 1]:
                            enemy_index = (self.choose_enemy(
                                output, player_indicator,
                                opposite_player_indicator, output[pos + line_len + 1]))
                            enemy = self.spawnlist[
                                self.spawnedplayers[enemy_index]]
                            enemyname = self.spawnedplayers[enemy_index]
                            self.fight(output, real_player, enemy, player, enemyname, pos,
                                       pos + line_len + 1, player_indicator,
                                       self.filepath)
                        else:
                            output[pos] = '.'
                            output[pos + line_len + 1] = player_indicator
                            self.reinitialize_file(self.filepath, output)

                    elif direction == "right" and output[pos + 1] != '#':
                        if opposite_player_indicator == output[pos + 1]:
                            enemy_index = (self.choose_enemy(
                                output, player_indicator,
                                opposite_player_indicator, output[pos + 1]))
                            enemy = self.spawnlist[
                                self.spawnedplayers[enemy_index]]
                            enemyname = self.spawnedplayers[enemy_index]
                            self.fight(output, real_player, enemy, player, enemyname, pos,
                                       pos + 1, player_indicator,
                                       self.filepath)
                        else:
                            if output[pos + 1] == 'W':
                                ###############################################
                                print (real_player.var)
                                entities[0].equip_weapon(weapons[0])
                                output[pos] = '.'
                                output[pos + 1] = player_indicator
                                self.reinitialize_file(self.filepath, output)

                    elif (direction == "left" and n != 0 and
                          output[pos - 1] != '#'):
                        if opposite_player_indicator == output[pos - 1]:
                            enemy_index = (self.choose_enemy(
                                output, player_indicator,
                                opposite_player_indicator, output[pos - 1]))
                            enemy = self.spawnlist[
                                self.spawnedplayers[enemy_index]]
                            enemyname = self.spawnedplayers[enemy_index]
                            self.fight(output, real_player, enemy, player, enemyname, pos,
                                       pos - 1, player_indicator,
                                       self.filepath)
                        else:
                            output[pos] = '.'
                            output[pos - 1] = player_indicator
                            self.reinitialize_file(self.filepath, output)

                    return True
                    break
        return False

    def choose_enemy(self, content, indicator1, indicator2, current_spot):
        count = -1
        if indicator1 in "".join(content) or indicator2 in "".join(content):
            for n, i in enumerate(content):
                if i == indicator1 or i == indicator2:
                    count += 1
                    if i == indicator2:
                        return count
                        break

    def fight(self, output, player1, player2, p1name, p2name, pos1, pos2, ind1, path):
        fight = Fight(player1, player2)
        winner = fight.simulate_fight()
        if winner == player1:
            output[pos1] = "."
            output[pos2] = ind1
            del self.spawnlist[p2name]
            self.spawnedplayers.remove(p2name)
        elif winner == player2:
            output[pos1] = "."
            del self.spawnlist[p1name]
            self.spawnedplayers.remove(p1name)

        self.reinitialize_file(path, output)

    def spawn_weapons(self):
        output = []
        free_slots = []
        f = open(self.filepath, "r+")
        output += f.read()
        f.close()
        if "." in "".join(output):
            for i in range(0, len(output)):
                if output[i] == '.':
                    free_slots.append(i)
                if output[i] == '\n' and output[i + 1] == '\n':
                    end_of_map = i + 1
                    break

        weapon_name = ""
        weapon_damage = ""
        weapon_crit = ""
        start_from = end_of_map + 1
        for x in range(0, 3):
            for i in range(start_from, len(output)):
                if output[i] != '\n':
                    if output[i] == ' ':
                        start_from = i + 1
                        break
                    if x == 0:
                        weapon_name += output[i]
                    elif x == 1:
                        weapon_damage += output[i]
                    elif x == 2:
                        weapon_crit += output[i]
        weapon_damage = int(weapon_damage)
        weapon_crit = float(weapon_crit)

        weapon = Weapon(weapon_name, weapon_damage, weapon_crit)
        global weapons
        weapons = []
        weapons.append(weapon)
        self.weapons[weapon_name] = weapon
        #random_slot = randint(0, len(free_slots))
        #output[free_slots[random_slot]] = 'W'
        output[1] = 'W'
        self.reinitialize_file(self.filepath, output)


orc = Orc("2", 100, 1.3)
hero1 = Hero("1", 100, "Tester")
testmap = Dungeon('testmap')
testmap.spawn_weapons()
testmap.spawn("1", hero1)
testmap.spawn("2", orc)
print (testmap.print_map())

# print (testmap.spawnlist)
# print (testmap.spawnedplayers)

testmap.move("1", "right")
print (hero1.has_weapon())
testmap.print_map()
print (entities)
