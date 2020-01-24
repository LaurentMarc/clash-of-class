import character

rogeranium = character.Wizard("Rogeranium")
zugugbug = character.Wizard("Zugugbug")

weapon, dmg = rogeranium.attack()

print("\n" +str(rogeranium) +" utilise " +weapon +" et inflige " +str(dmg) +" pts de dégats.")

print("\n" +str(zugugbug) +" se défend et contre " +str(zugugbug.defend(weapon, dmg)) +" pts de dégats.")

print("\nIl reste : " +str(zugugbug.current_life) + " PV à " +str(zugugbug))
