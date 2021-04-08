class Inventory:
    __capacity = 0

    def __init__(self, capacity):
        Inventory.__capacity = capacity
        self.items = []

    def add_item(self, item):
        if len(self.items) < Inventory.__capacity:
            self.items.append(item)
            return
        return "not enough room in the inventory"

    def get_capacity(self):
        return Inventory.__capacity

    def __repr__(self):
        free_storage = Inventory.__capacity - len(self.items)
        items_joined = ', '.join(self.items)
        return f"Items: {items_joined}.\nCapacity left: {free_storage}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
