import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50

    def eat(self):
        print(f"{self.name} поїв.")
        self.hunger -= 20
        self.energy += 10

    def sleep(self):
        print(f"{self.name} поспав.")
        self.energy += 30

    def play(self):
        print(f"{self.name} погрався.")
        self.hunger += 20
        self.energy -= 20

    def live(self):
        action = random.choice([self.eat, self.sleep, self.play])
        action()
        print(f"Статус -> Голод: {self.hunger}, Енергія: {self.energy}\n")

my_cat = Cat("Барсік")

for day in range(1, 4):
    print(f"День {day}:")
    my_cat.live()