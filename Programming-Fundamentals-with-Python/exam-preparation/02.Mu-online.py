dungeon_rooms = input().split("|")

initial_health = 100
initial_bitcoin = 0

best_room_value = 0
room_n = 0
best_room = 0

for room in dungeon_rooms:
    command, value = room.split()
    room_n += 1
    if command == "potion":
        if (initial_health + int(value)) > 100:
            health = initial_health
            initial_health = 100
            print(f"You healed for {100 - health} hp.")
            print(f"Current health: {initial_health} hp.")
            continue
        initial_health += int(value)
        print(f"You healed for {int(value)} hp.")
        print(f"Current health: {initial_health} hp.")
    elif command == "chest":
        initial_bitcoin += int(value)
        print(f"You found {int(value)} bitcoins.")
    else:
        initial_health -= int(value)
        if initial_health > 0:
            print(f"You slayed {command}.")
            if int(value) > best_room_value:
                best_room_value = int(value)
                best_room = room
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_n}")
            break

if initial_health > 0:
    print(f"You've made it!")
    print(f"Bitcoins: {initial_bitcoin}")
    print(f"Health: {initial_health}")
