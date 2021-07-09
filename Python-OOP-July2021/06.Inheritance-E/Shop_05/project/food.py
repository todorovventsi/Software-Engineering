from project.product import Product


class Food(Product):
    FOOD_DEFAULT_QUANTITY = 15

    def __init__(self, name):
        super().__init__(name, self.FOOD_DEFAULT_QUANTITY)
