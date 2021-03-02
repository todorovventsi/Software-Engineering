pr_quantities = input().split()
searched_products = input().split()

products = {}
for index in range(0, len(pr_quantities), 2):
    key = pr_quantities[index]
    value = int(pr_quantities[index + 1])
    products[key] = value

for product in searched_products:
    if product in products:
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
