class ProductRepository:
    def __init__(self, products = []):
        self.products = products

    def add(self, product):
        self.products.append(product)

    def find(self, product):
        for item in self.products:
            if product == item.name:
                return item

    def remove(self, product_name):
        for item in self.products:
            if product_name == item.name:
                self.products.remove(item)

    def __repr__(self):
        result = [f"{item.name}: {item.quantity}\n" for item in self.products]
        return f"{''.join(result)}"
