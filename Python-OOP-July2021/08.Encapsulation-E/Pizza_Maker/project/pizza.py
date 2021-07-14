from collections import defaultdict


class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = defaultdict(lambda: 0)
        self.__toppings_number = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = value

    def add_topping(self, topping):
        if self.toppings_capacity > self.__toppings_number:
            self.toppings[topping.topping_type] += topping.weight
            self.__toppings_number += 1
            return
        raise ValueError("Not enough space for another topping")

    def calculate_total_weight(self):
        return self.dough.weight + sum(weight for weight in self.toppings.values())
