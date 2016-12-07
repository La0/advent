import re
from collections import namedtuple

Item = namedtuple('Item', 'name,cost,damage,armor')

class RPG(object):
    """
    RPG Simulator !
    """
    def __init__(self, filename, hit):
        self.hit = hit

        # Load inventory
        self.shop = {}
        item = re.compile(r'^([\w \+]+)\s+(\d+)\s+(\d+)\s+(\d+)')
        cat = re.compile(r'^(\w+):\s+(\w+)\s+(\w+)\s+(\w+)')
        with open(filename, 'r') as f:
            for line in f.readlines():
                res = cat.match(line)
                if res:
                    category = res.group(1).lower()[0]
                    self.shop[category] = []
                else:
                    res = item.match(line)
                    if res:
                        i = res.groups()
                        self.shop[category].append(Item(i[0].strip(), int(i[1]), int(i[2]), int(i[3])))

    def battle(self, hit=0, damage=0, armor=0):
        """
        Battle an enemy described as abor
        """
        # Pick one weapon (mandatory)
        # List all possible gear
        def __gear(gear, comb, nb):
            if not comb:
                g = list(gear) # clone
                if len(g) == nb:
                    gears.append((g, sum([i.cost for i in g])))
                return
            for item in self.shop[comb[0]]:
                if item in gear:
                    continue
                gear.append(item)
                __gear(gear, comb[1:], nb)
                gear.pop()

        #List all gear combinations
        combs = [
            'w',
            'wr',
            'wrr',
            'wa',
            'war',
            'warr',
        ]
        gears = []
        for comb in combs:
            __gear([], comb, len(comb))

        # Sorted by cost
        gears = sorted(gears, key=lambda x : x[1])

        # Do i win with this gear ?
        def __win(gear):
            my_damage = sum([i.damage for i in gear])
            my_armor = sum([i.armor for i in gear])

            enemy_hits = max(damage - my_armor, 1)
            my_hits = max(my_damage - armor, 1)

            enemy_ratio = 1.0 * hit / my_hits
            my_ratio = 1.0 * self.hit / enemy_hits

            return enemy_ratio < my_ratio

        # Find highest cost to lose
        best = max([cost for g, cost in gears if not __win(g)])
        for g in [g for g,c in gears if c == best]:
            print g

        return best

if __name__ == '__main__':
    rpg = RPG('21.input', 100)
    print rpg.battle(hit=109, damage=8, armor=2)
