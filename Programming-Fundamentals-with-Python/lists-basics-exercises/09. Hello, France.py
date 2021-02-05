given_items = input().split("|")
total_budget = float(input())

bought_items = []
profit = 0

for item in given_items:
    current_item = item.split("->")
    item_price = float(current_item[-1])

    # Price validation:
    if "Clothes" in item and item_price > 50:
        continue
    elif "Shoes" in item and item_price > 35:
        continue
    elif "Accessories" in item and item_price > 20.5:
        continue

    # Budget validation:
    if total_budget < item_price:
        continue

    # Buying item:
    total_budget -= item_price
    new_item_price = item_price * 1.4
    bought_items.append(new_item_price)
    profit += item_price * 0.4

new_budget = total_budget + sum(bought_items)

for item in bought_items:
    print(f"{item:.2f}", end= " ")

print(f"\nProfit: {profit:.2f}")
if new_budget <= 150:
    print("Time to go.")
else:
    print("Hello, France!")
