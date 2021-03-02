data = input().split()

products = {}

for index in range(0, len(data), 2):
    c_product = data[index]
    quantity = int(data[index + 1])
    products[c_product] = quantity

print(products)