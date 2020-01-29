from random import randint


class Player:
    max_life_pts = 12
    magic_dice = 12
    sword_dice = 8
    bow_dice = 10
    bow_bonus = 0
    sword_bonus = 0
    bonus_dmg = 0

    def __init__(self, name):
        self._current_life = self.max_life_pts
        self.name = name
        self._weight = randint(70, 90)
        self._height = randint(170, 190)

    def __repr__(self):
        return self.name + " the " + self.__class__.__name__

    # PROPRIETE POIDS PERSONNAGE

    def get_weight(self):
        return self._weight

    def set_weight(self, value):
        self._weight = value

    weight = property(get_weight, set_weight)

    # /PROPRIETE POIDS PERSONNAGE

    # PROPRIETE TAILLE PERSONNAGE

    def get_height(self):
        return self._height

    def set_height(self, value):
        self._height = value

    height = property(get_height, set_height)

    # /PROPRIETE TAILLE PERSONNAGE

    # PROPRIETE VIE ACTUELLE PERSONNAGE

    def set_current_life(self, value):
        self._current_life = max(min(self.max_life_pts, value), 0)

    def get_current_life(self):
        return self._current_life

    current_life = property(get_current_life, set_current_life)

    # /PROPRIETE VIE ACTUELLE PERSONNAGE

    def roll_dices(self):
        dices = [["magic", randint(1, self.magic_dice)], ["sword", randint(1, self.sword_dice)],
                 ["bow", randint(1, self.bow_dice)]]
        return dices

    def attack(self):
        dices = self.roll_dices()
        result_atk = sorted(dices, key=lambda x: x[1], reverse=True)
        result_atk = result_atk[0]
        result_atk = {"weapon": result_atk[0], "dmg": result_atk[1], "bonus_dmg": self.bonus_dmg}
        if result_atk["weapon"] == "sword":
            result_atk["dmg"] += self.sword_bonus
        if result_atk["weapon"] == "bow":
            result_atk["dmg"] += self.bow_bonus
        return result_atk

    def defend(self, weapon, dmg):
        dices = dict(self.roll_dices())
        defend_value = dices[weapon]
        if defend_value < dmg:
            new_current_life = self.current_life - (dmg - defend_value)
            self.current_life = new_current_life
        return defend_value

    # RACES
class Dwarf:

    sword_bonus = 2

class Elf:

    bow_bonus = 2

    # /RACES

    # CLASSES

class Wizard(Player):

    def attack(self):
        result_atk = super().attack()
        second_magic_dice = dict(self.roll_dices())["magic"]
        if second_magic_dice > result_atk["dmg"]:
            return {"weapon": "magic", "dmg": second_magic_dice, "bonus_dmg": self.bonus_dmg}
        if result_atk["weapon"] == "sword":
            self.bonus_dmg += (self.weight + self.height) // 40
        if result_atk["weapon"] == "bow":
            self.bonus_dmg += (self.height - 170) % 3
        result_atk["dmg"] += result_atk["bonus_dmg"]
        return result_atk


class Warrior(Player):
    sword_dice = 12
    magic_dice = 8
    max_life_pts = 16

    def attack(self):
        result_atk = super().attack()
        if result_atk["weapon"] == "magic":
            self.bonus_dmg += self.weight // 30
        if result_atk["weapon"] == "bow":
            self.bonus_dmg = (self.height - 170) % 3
        result_atk["dmg"] += self.bonus_dmg
        return result_atk


class Archer(Player):
    bow_dice = 12
    magic_dice = 10

    def attack(self):
        result_atk = super().attack()
        if result_atk["weapon"] == "sword":
            self.bonus_dmg += (self.height // 40) + 1
        if result_atk["weapon"] == "magic":
            self.bonus_dmg += (self.weight // 20) + 1
        result_atk["dmg"] += self.bonus_dmg
        return result_atk

    #/ CLASSES

class ElfWizard(Elf, Wizard):
    pass

class DwarfWizard(Dwarf, Wizard):
    pass

class ElfArcher(Elf, Archer):
    pass

class DwarfArcher(Dwarf, Archer):
    pass

class ElfWarrior(Elf, Warrior):
    pass

class DwarfWarrior(Dwarf, Warrior):
    pass
