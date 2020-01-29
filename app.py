import character
import random

def main():

    rogeranium = character.ElfArcher("Rogeranium")
    zugugbug = character.ElfWizard("Zugugbug")
    trololo = character.ElfWarrior("Trololo")
    gandalf = character.DwarfWizard("Gandalf")
    martymcfly = character.DwarfWarrior("Marty Mc Fly")
    docbrown = character.DwarfArcher("Doc Brown")


    characters = [rogeranium, zugugbug, trololo, gandalf, martymcfly, docbrown]
    attacker = random.choice(characters)
    defender = random.choice(characters)
    while attacker == defender:
        defender = random.choice(characters)
    attacker_turn = True
    defender_turn = False

    while defender.current_life > 0 and attacker.current_life > 0:
        while attacker_turn and attacker.current_life > 0:
            atk_result = attacker.attack()
            def_result = defender.defend(atk_result["weapon"], atk_result["dmg"])
            print("\n",attacker, "utilise", atk_result["weapon"], "et inflige", atk_result["dmg"], "pts de dégats, dont", atk_result["bonus_dmg"], "pts de dégats bonus.")
            print("\n", defender, "se défend et contre", def_result, "pts de dégats.")
            print("\nIl reste :", defender.current_life, " PV à ", defender)
            print("\n _________________________________________________________________")
            attacker_turn = False
            defender_turn = True
        while defender_turn and defender.current_life > 0:
            atk_result = defender.attack()
            def_result = attacker.defend(atk_result["weapon"], atk_result["dmg"])
            print("\n", defender,"rispote et inflige", atk_result["dmg"],"pts de dégats avec", atk_result["weapon"])
            print("\n", attacker, "se défend et contre", def_result, "pts de dégats.")
            print("\n", "il reste :", attacker.current_life, "PV à", attacker)
            print("\n _________________________________________________________________")
            defender_turn = False
            attacker_turn = True
    if defender.current_life == 0 or attacker.current_life == 0:
        if defender.current_life == 0:
            print("\n", defender, "s'est fait casser la gueule ! HA-HA !")
        else:
            print("\n", attacker, "s'est fait casser la gueule ! HA-HA !")

if __name__ == "__main__":
    main()
