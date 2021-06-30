class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity
        self.space = size - quantity

    def fill(self, milliliters):
        if self.space >= milliliters:
            self.quantity += milliliters
            self.space -= milliliters

    def status(self):
        return self.space


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
