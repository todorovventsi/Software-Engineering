from collections import deque


def stock_availability(inv, command, *args):
    inventory = deque(inv)
    if command == "delivery":
        for stock in args:
            inventory.append(stock)
    elif command == "sell":
        if not args:
            inventory.popleft()
        for arg in args:
            if isinstance(arg, int):
                for _ in range(arg):
                    inventory.popleft()
            elif isinstance(arg, str):
                while arg in inventory:
                    inventory.remove(arg)
    return list(inventory)

print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
