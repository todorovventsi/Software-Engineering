import re
from statistics import mean

n_of_plants = int(input())
plants_register = {}
for _ in range(n_of_plants):
    plant, rarity = input().split("<->")
    if plant not in plants_register:
        plants_register[plant] = {"rarity": 0, "ratings": []}
    plants_register[plant]["rarity"] = int(rarity)

command = input()
plant_pattern = r"(?<=: )[a-zA-Z]+\b"
stats_pattern = r"(?<=- )[0-9]+$"
while not command == "Exhibition":
    data = command
    plant = re.search(plant_pattern, data).group()
    if plant not in plants_register:
        print("error")
        command = input()
        continue
    if "Rate" in data:
        rating = int(re.search(stats_pattern, data).group())
        plants_register[plant]["ratings"].append(rating)
    elif "Update" in data:
        new_rarity = int(re.search(stats_pattern, data).group())
        plants_register[plant]["rarity"] = new_rarity
    elif "Reset" in data:
        plants_register[plant]["ratings"].clear()
    command = input()

for value in plants_register.values():
    if value["ratings"]:
        value["ratings"] = mean(value["ratings"])
    else:
        value["ratings"] = 0

plants_register = sorted(plants_register.items(), key=lambda kvp: (-kvp[1]["rarity"], -kvp[1]["ratings"]))
print("Plants for the exhibition:")
for plant, stats in plants_register:
    print(f"- {plant}; Rarity: {stats['rarity']}; Rating: {stats['ratings']:.2f}")
