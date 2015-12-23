# Magic Missile costs 53 mana. It instantly does 4 damage.
def magic_missile(hero, boss):
    boss.hit -= 4

#Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
def drain(hero, boss):
    hero.hit += 2
    boss.hit -= 2

#Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
def shield(hero, boss):

    def _boost_armor(hero, boss):
        hero.armor = 7
    def _restore_armor(hero, boss):
        hero.armor = 0

    return [_boost_armor, ] * 6 + [_restore_armor, ]

#Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
def poison(hero, boss):

    def _poison(hero, boss):
        boss.hit -= 3

    return [_poison, ] * 6

#Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.
def recharge(hero, boss):

    def _boost_mana(hero, boss):
        hero.mana += 101

    return [_boost_mana, ] * 5


class Player(object):
    def __init__(self, name, hit=0, mana=0, damage=0):
        self.name = name
        self.hit = hit
        self.mana = mana
        self.armor = 0
        self.damage = damage

    @property
    def is_dead(self):
        return self.hit <= 0

    def __str__(self):
        if self.is_dead:
            return '%s dead !' % self.name
        return '%s %d hits' % (self.name, self.hit)

# All spells with costs
all_spells = {
    magic_missile : 53,
    drain : 73,
    shield : 113,
    poison : 173,
    recharge : 229,
}


def battle(hero, boss, spells, hard=False):
    """
    Run battle with spells listed
    Outcomes are :
    * win, when the hero wins
    * lose, when the hero loses
    * invalid, when the spells list is invalid
    * moar, when the hero needs more spells
    """
    effects = {}
    step = 0
    while True:
        # Run current after effects
        for k,v in effects.items():
            e = v[0]
            e(hero, boss)
            # print 'Running effect', e.func_name
            del v[0]
            if not v:
                del effects[k]

        # print 'Step %d' % step
        if step % 2 == 0:
            if hard:
                hero.hit -= 1
                if hero.is_dead:
                    return 'lose'

            # Play magician
            # No more spell ?
            if step / 2 >= len(spells):
                return 'moar'

            spell = spells[step/2]

            # no more mana ?
            cost = all_spells[spell]
            if hero.mana < cost:
                return 'lose'

            # Check spell is not in effects
            if spell in effects:
                return 'invalid'

            # Run spell
            # print 'Running', spell.func_name
            # Remove mana used by spell
            after = spell(hero, boss)
            hero.mana -= cost
            if after:
                # Run first effect
                after[0](hero, boss)
                del after[0]

                # Save after effects
                effects[spell] = after

            # print 'Hero -> %s' % boss

        else:
            # Play boss
            damage = max(1, boss.damage - hero.armor)
            hero.hit -= damage
            # print 'Boss -> %s' % hero

        # Win / lose ?
        if hero.is_dead:
            return 'lose'
        if boss.is_dead:
            return 'win'

        step += 1


def optimal_battle(hard=False):
    """
    Find optimal spell sequence
    against described enemy
    """
    winners = []

    def _run(spells, best_cost):
        for spell in all_spells.keys():
            spells.append(spell)

            # Calc cost to skip useless battles
            cost = sum([all_spells[s] for s in spells])
            if cost < best_cost:

                # Battle with this spells list
                hero = Player('Hero', hit=50, mana=500)
                boss = Player('Boss', hit=71, damage=10)
                outcome = battle(hero, boss, spells, hard=hard)
                # print outcome
                if outcome == 'win':
                    if cost < best_cost:
                        # Save this spells list
                        print cost, ', '.join(map(lambda x : x.func_name, spells))
                        winners.append(list(spells))
                        best_cost = cost
                elif outcome == 'moar':
                    # Add more spells
                    best_cost = min(best_cost, _run(spells, best_cost))
                else:
                    # Don't progress further
                    pass

            spells.pop()

        return best_cost


    return _run([], float('inf'))


if __name__ == '__main__':
    print optimal_battle(True)
