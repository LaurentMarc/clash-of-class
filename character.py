from random import randint

class Player:

    max_life_pts = 12
    magic_dice = 12
    sword_dice = 8
    bow_dice = 10
    current_life = max_life_pts

    def roll_dices(self):
        dices = [["magic", randint(1, self.magic_dice)], ["sword", randint(1, self.sword_dice)], ["bow", randint(1, self.bow_dice)]]
        return dices

    def attack(self):
        dices = self.roll_dices()
        result_atk = sorted(dices, key=lambda x: x[1], reverse=True)
        return result_atk[0]

    def defend(self, weapon, dmg):
        dices = dict(self.roll_dices())
        defend_value = dices[weapon]
        if defend_value < dmg:
            self.current_life -= (dmg - defend_value)
        return defend_value


class Wizard(Player):

    def __init__(self, name):
        self.current_life = self.max_life_pts
        self.name = name

    def __repr__(self):
        return self.name +" the " +Wizard.__name__
