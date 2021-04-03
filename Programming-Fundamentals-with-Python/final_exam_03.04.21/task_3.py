people = {}

command = input()
while not command == "Results":
    data = command.split(":")
    if "Add" in data:
        name = data[1]
        health = int(data[2])
        energy = int(data[3])
        if name not in people:
            people[name] = {"health": health, "energy": energy}
            command = input()
            continue
        people[name]["health"] += health
    elif "Attack" in data:
        attacker = data[1]
        defender = data[2]
        damage = int(data[3])
        if attacker in people and defender in people:
            people[defender]["health"] -= damage
            people[attacker]["energy"] -= 1
            if people[defender]["health"] <= 0:
                people.pop(defender)
                print(f"{defender} was disqualified!")
            if people[attacker]["energy"] <= 0:
                people.pop(attacker)
                print(f"{attacker} was disqualified!")
    elif "Delete" in data:
        to_delete = data[1]
        if to_delete == "All":
            people.clear()
            command = input()
            continue
        people.pop(to_delete)

    command = input()

ppl_left = len(people)

people = sorted(people.items(), key=lambda kvp: (-kvp[1]["health"], kvp[0]))
print(f"People count: {ppl_left}")
for person, stats in people:
    print(f"{person} - {stats['health']} - {stats['energy']} ")
