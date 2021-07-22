from project.animals.animal import Bird
from project.food import Vegetable, Meat, Fruit, Seed


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.foods = [Meat]
        self.kilos_per_food = 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.foods = [Meat, Vegetable, Fruit, Seed]
        self.kilos_per_food = 0.35

    def make_sound(self):
        return "Cluck"
