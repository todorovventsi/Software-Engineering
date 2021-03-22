import re

text_line = input()
pattern = r'>>(?P<furniture>[a-zA-Z0-9]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)'
spend_money = 0
furniture_bought = []

while not text_line == "Purchase":
    register = [item.groupdict() for item in re.finditer(pattern, text_line)]
    if register:
        furniture_bought.append(register[0]["furniture"])
        spend_money += float(register[0]['price']) * int(register[0]['quantity'])
        register = []

    text_line = input()

print("Bought furniture:")
if furniture_bought:
    print(*furniture_bought, sep= "\n")
print(f"Total money spend: {spend_money:.2f}")
