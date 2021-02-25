treasure_chest = input().split("|")

command = input()

while not command == "Yohoho!":
    if "Loot" in command:
        loot = command.split()
        loot.remove("Loot")
        for item in loot:
            if item not in treasure_chest:
                treasure_chest.insert(0, item)
        # treasure_chest = list(set(loot + treasure_chest))

    elif "Drop" in command:
        command = command.split()
        index = int(command[1])
        if index in range(len(treasure_chest)):
            item = treasure_chest[index]
            treasure_chest.remove(item)
            treasure_chest.append(item)

    elif "Steal" in command:
        command = command.split()
        count = int(command[1])
        stolen_item = []
        for _ in range(count):
            if not treasure_chest:
                break
            stolen_item.append(treasure_chest.pop())
        stolen_item.reverse()
        print(*stolen_item, sep=", ")

    command = input()

if treasure_chest:
    length = "".join(treasure_chest)
    mean_gain = len(length) / len(treasure_chest)
    print(f"Average treasure gain: {mean_gain:.2f} pirate credits.")
else:
    print(f"Failed treasure hunt.")
