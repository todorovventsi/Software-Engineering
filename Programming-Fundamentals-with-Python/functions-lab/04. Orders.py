def order_price_calculation(product, quantity):
    price = None
    if product == "coffee":
        price = 1.5
    elif product == "water":
        price = 1.0
    elif product == "coke":
        price = 1.4
    elif product == "snack":
        price = 2.0
    return price * quantity


order_product = input()
order_quantity = int(input())
order_price = order_price_calculation(order_product, order_quantity)
print(f"{order_price:.2f}")
