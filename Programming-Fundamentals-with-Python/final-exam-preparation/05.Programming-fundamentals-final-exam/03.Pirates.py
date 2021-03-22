destinations = {}

f_command = input()
while not f_command == "Sail":
    town, people, gold = f_command.split("||")
    if town not in destinations:
        destinations[town] = {"population": 0, "treasury": 0}
    destinations[town]["population"] += int(people)
    destinations[town]["treasury"] += int(gold)

    f_command = input()

s_command = input()
while not s_command == "End":
    data = s_command.split("=>")
    if "Plunder" in data:
        town = data[1]
        people = int(data[2])
        gold = int(data[3])
        if town in destinations:
            destinations[town]["population"] -= people
            destinations[town]["treasury"] -= gold
            if destinations[town]["population"] <= 0 or destinations[town]["treasury"] <= 0:
                destinations.pop(town)
                print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
                print(f"{town} has been wiped off the map!")
                continue
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    elif "Prosper" in data:
        town = data[1]
        gold = int(data[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            s_command = input()
            continue
        destinations[town]["treasury"] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {destinations[town]['treasury']} gold.")

    s_command = input()


if destinations:
    destinations = dict(sorted(destinations.items(), key=lambda kvp: (-int(kvp[1]['treasury']), kvp[0])))
    print(f"Ahoy, Captain! There are {len(destinations)} wealthy settlements to go to:")
    for town in destinations:
        print(f"{town} -> Population: {destinations[town]['population']} citizens, Gold: {destinations[town]['treasury']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
