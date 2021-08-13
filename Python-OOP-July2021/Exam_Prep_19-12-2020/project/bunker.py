class Bunker:

    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        foods = [food for food in self.supplies if food.__class__.__name__ == "FoodSupply"]
        if foods:
            return foods
        raise IndexError("There are no food supplies left!")

    @property
    def water(self):
        water = [w for w in self.supplies if w.__class__.__name__ == "WaterSupply"]
        if water:
            return water
        raise IndexError("There are no water supplies left!")

    @property
    def painkillers(self):
        painkillers = [p for p in self.medicine if p.__class__.__name__ == "Painkiller"]
        if painkillers:
            return painkillers
        raise IndexError("There are no painkillers left!")

    @property
    def salves(self):
        salves = [s for s in self.medicine if s.__class__.__name__ == "Salve"]
        if salves:
            return salves
        raise IndexError("There are no salves left!")

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        to_remove_med = [m for m in self.medicine if m.__class__.__name__ == medicine_type][-1]
        self.medicine.remove(to_remove_med)
        if survivor.needs_healing:
            to_remove_med.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        to_remove_supply = [s for s in self.supplies if s.__class__.__name__ == sustenance_type][-1]
        self.supplies.remove(to_remove_supply)
        if survivor.needs_sustenance:
            to_remove_supply.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= (survivor.age * 2)
        for survivor in self.survivors:
            self.sustain(survivor, "FoodSupply")
            self.sustain(survivor, "WaterSupply")
