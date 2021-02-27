import math

budget = float(input())
students = int(input())
price_of_flour = float(input())
price_of_egg = float(input())
price_of_apron = float(input())

total_price = price_of_apron * (students + math.ceil(students * 0.2)) + price_of_egg * 10 * students + price_of_flour * (students - students // 5)

diff = abs(budget - total_price)
if total_price <= budget:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    print(f"{diff:.2f}$ more needed.")
