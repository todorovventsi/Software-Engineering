from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, kilometers):
        pass

    @abstractmethod
    def refuel(self, liters):
        pass


class Car(Vehicle):

    def drive(self, kilometers):
        if kilometers * (self.fuel_consumption + 0.9) <= self.fuel_quantity:
            self.fuel_quantity -= kilometers * (self.fuel_consumption + 0.9)

    def refuel(self, liters):
        self.fuel_quantity += liters


class Truck(Vehicle):

    def drive(self, kilometers):
        if kilometers * (self.fuel_consumption + 1.6) <= self.fuel_quantity:
            self.fuel_quantity -= kilometers * (self.fuel_consumption + 1.6)

    def refuel(self, liters):
        self.fuel_quantity += (liters * 0.95)


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
