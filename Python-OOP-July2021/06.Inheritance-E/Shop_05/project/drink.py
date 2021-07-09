from project.product import Product


class Drink(Product):
    DRINK_DEFAULT_QUANTITY = 10

    def __init__(self, name):
        super().__init__(name, self.DRINK_DEFAULT_QUANTITY)
