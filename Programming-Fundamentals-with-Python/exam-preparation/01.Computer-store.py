net_price = 0

component_price = input()

while not (component_price == "special" or component_price == "regular"):
    if float(component_price) >= 0:
        net_price += float(component_price)
    else:
        print("Invalid price!")
    component_price = input()

taxes_over_price = 0.2 * net_price

total_price = net_price + taxes_over_price
if component_price == "special":
    total_price *= 0.9
if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {net_price:.2f}$")
    print(f"Taxes: {taxes_over_price:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")
