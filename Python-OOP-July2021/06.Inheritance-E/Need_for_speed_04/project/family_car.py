from project.car import Car


class FamilyCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 3

    def __init__(self, fuel, horse_power, fuel_consumption=DEFAULT_FUEL_CONSUMPTION):
        super().__init__(fuel, horse_power, fuel_consumption)
