import re

text_line = input()
pattern = r'>>(?P<furniture>[a-zA-Z0-9]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)'
spend_money = 0
furniture_bought = []

while not text_line == "Purchase":
    register = re.match(pattern, text_line)  # USING MATCH() BECAUSE ONLY ONE OCCURRENCE IS EXPECTED
    if register:
        register = register.groupdict()
        furniture_bought.append(register["furniture"])
        spend_money += float(register["price"]) * int(register["quantity"])

    text_line = input()

print("Bought furniture:")
if furniture_bought:
    print(*furniture_bought, sep="\n")
print(f"Total money spend: {spend_money:.2f}")
