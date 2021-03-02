products = {}

data = input()
while not data == "statistics":
    product, value = data.split(": ")
    value = int(value)
    if product not in products:
        products[product] = 0
    products[product] += value

    data = input()

print("Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
