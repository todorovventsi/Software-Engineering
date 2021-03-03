products = {}

order = input()

while not order == "buy":
    current_product, product_price, product_quantity = order.split()
    product_price = float(product_price)
    product_quantity = int(product_quantity)

    if current_product not in products:
        products[current_product] = []
        products[current_product].append(product_price)
        products[current_product].append(product_quantity)
    else:
        products[current_product][0] = product_price
        products[current_product][1] += product_quantity

    order = input()

for product, value in products.items():
    total_price = value[0] * value[1]
    print(f"{product} -> {total_price:.2f}")
