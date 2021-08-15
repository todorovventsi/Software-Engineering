from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:

    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value == " ":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type, name, price):
        if food_type == "Bread":
            current_food = Bread(name, price)
        else:
            current_food = Cake(name, price)
        foods = [f for f in self.food_menu if f.name == name]
        if foods:
            raise Exception(f"{food_type} {name} is already in the menu!")
        self.food_menu.append(current_food)
        return f"Added {current_food.name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        if drink_type == "Tea":
            current_drink = Tea(name, portion, brand)
        else:
            current_drink = Water(name, portion, brand)
        drinks = [d for d in self.drinks_menu if d.name == name]
        if drinks:
            raise Exception(f"{drink_type} {name} is already in the menu!")
        self.drinks_menu.append(current_drink)
        return f"Added {current_drink.name} ({current_drink.brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        if table_type == "InsideTable":
            current_table = InsideTable(table_number, capacity)
        else:
            current_table = OutsideTable(table_number, capacity)
        tables = [t for t in self.tables_repository if t.table_number == table_number]
        if tables:
            raise Exception(f"Table {table_number} is already in the bakery!")
        self.tables_repository.append(current_table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        for table in self.tables_repository:
            if not table.is_reserved:
                if table.capacity >= number_of_people:
                    table.reserve(number_of_people)
                    return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number, *args):
        table = None
        for t in self.tables_repository:
            if t.table_number == table_number:
                table = t
        if table is None:
            return f"Could not find table {table_number}"
        foods_in_menu = []
        foods_not_in_menu = []
        for food in args:
            foods = [f for f in self.food_menu if food == f.name]
            if foods:
                foods_in_menu.append(foods[0])
            else:
                foods_not_in_menu.append(food)
        for food in foods_in_menu:
            table.order_food(food)
        nl = '\n'
        ordered_foods_msg = [repr(f) for f in foods_in_menu]
        return f"Table {table_number} ordered:\n{nl.join(ordered_foods_msg)}\n{self.name} does not have in the menu:\n{nl.join(foods_not_in_menu)}"

    def order_drink(self, table_number, *args):
        table = None
        for t in self.tables_repository:
            if t.table_number == table_number:
                table = t
        if table is None:
            return f"Could not find table {table_number}"
        drinks_in_menu = []
        drinks_not_in_menu = []
        for drink in args:
            drinks = [d for d in self.drinks_menu if drink == d.name]
            if drinks:
                drinks_in_menu.append(drinks[0])
            else:
                drinks_not_in_menu.append(drink)
        for drink in drinks_in_menu:
            table.order_drink(drink)
        nl = '\n'
        ordered_drinks_msg = [repr(d) for d in drinks_in_menu]
        return f"Table {table_number} ordered:\n{nl.join(ordered_drinks_msg)}\n{self.name} does not have in the menu:\n{nl.join(drinks_not_in_menu)}"

    def leave_table(self, table_number):
        table = None
        for t in self.tables_repository:
            if t.table_number == table_number:
                table = t
        bill = table.get_bill()
        self.total_income += bill
        table.clear()
        return f"Table: {table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        free_tables = [table for table in self.tables_repository if not table.is_reserved]
        info_msg = [f"{table.free_table_info()}" for table in free_tables]
        nl = '\n'
        return f"{nl.join(info_msg)}"

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
