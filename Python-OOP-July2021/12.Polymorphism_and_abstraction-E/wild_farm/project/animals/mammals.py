from project.animals.animal import Mammal
from project.food import Vegetable, Meat, Fruit, Seed


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.foods = [Vegetable, Fruit]
        self.kilos_per_food = 0.10

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.foods = [Meat]
        self.kilos_per_food = 0.40

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.foods = [Vegetable, Meat]
        self.kilos_per_food = 0.30

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.foods = [Meat]
        self.kilos_per_food = 1

    def make_sound(self):
        return "ROAR!!!"
