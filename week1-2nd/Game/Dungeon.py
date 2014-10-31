from hero import Hero
from orc import Orc


class Dungeon():
    spawnlist = {}
    spawnedplayers = []

    def __init__(self, filepath):
        self.filepath = filepath

    def print_map(self):
        f = open(self.filepath, "r+")
        map = f.read()
        f.close
        print(map)
        return map

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
        pos = self.get_player_position(player)
        output = []
        player_indicator = self.get_player_indicator(self.spawnlist[player])
        f = open(self.filepath, "r+")
        for line in f:
            line_len = len(line)
            break
        output += f.read()
        print (output)
        f.close()
        if player_indicator in "".join(output):
            print ("----------HERO FOUND ON MAP----------")
            for n, i in enumerate(output):
                if i == player_indicator and n != len(output) - 1:
                    print ("----------HERO MOVED ON MAP----------")
                    output[pos] = '.'
                    if direction == "up":
                        output[pos-line_len] = player_indicator
                    elif direction == "down":
                        output[pos+line_len] = player_indicator
                    elif direction == "right":
                        output[pos+1] = player_indicator
                    elif direction == "left":
                        output[pos-1] = player_indicator
                    return True
                    break

        f = open(self.filepath, "w+")
        f.write("".join(output))
        f.close()
        return False
