class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power, fuel_consumption=DEFAULT_FUEL_CONSUMPTION):
        self.fuel_consumption = fuel_consumption
        self.horse_power = horse_power
        self.fuel = fuel

    def drive(self, kilometers):
        if self.fuel >= self.fuel_consumption * kilometers:
            self.fuel -= self.fuel_consumption * kilometers
            return
