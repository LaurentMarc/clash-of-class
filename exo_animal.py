class Animal:

    hair_type = None
    life_esperance = None
    sound = None
    diet = []

    def __init__(self, name, weight, color, age):
        self.name = name
        self.weight = weight
        self.hair_type = color
        self.age = age

    def talk(self):
        return self.sound

    def eat(self, eated):
        for aliment in self.get_diet():
            if eated == aliment:
                self.weight += (self.weight * 0.05)
                return True
        return False


    def get_diet(self):
        return self.diet

    def get_age(self):
        return self._age

    def set_age(self, value):
        if 0 < value < self.life_esperance:
            self._age = value
        else:
            raise Exception("la valeur age n'est pas bonne")

    age = property(get_age, set_age)

class Cat(Animal):

    sound = "miaou"
    life_esperance = 15
    diet = ["croquette", "paté", "oiseau"]


class Snail(Animal):

    sound = "rien"
    life_esperance = 5
    diet = ["salade", "immeuble"]


class Snake(Animal):

    life_esperance = 10
    sound = "ssssss"
    diet = ["souris", "éléphant", "humain"]




ozzy = Cat("Ozzy", 100, "blanc", 3)
snail = Snail("escargot", 1000, "marron", 1)
snake = Snake("serpent", 5, "vert", 3)

print("\n", ozzy.name, ozzy.weight, ozzy.hair_type, ozzy.age)
print(ozzy.talk())
print(ozzy.get_diet())
print(str(ozzy.eat("paté")),ozzy.weight)
print(str(ozzy.eat("immeuble")),ozzy.weight)

print("\n", snail.name, snail.weight, snail.hair_type, snail.age)
print(snail.talk())
print(snail.get_diet())
print(str(snail.eat("immeuble")), snail.weight)
print(str(snail.eat("éléphant")), snail.weight)

print("\n", snake.name, snake.weight, snake.hair_type, snake.age)
print(snake.talk())
print(ozzy.get_diet())
print(str(snake.eat("éléphant")), snake.weight)
print(str(snake.eat("paté")), snake.weight)