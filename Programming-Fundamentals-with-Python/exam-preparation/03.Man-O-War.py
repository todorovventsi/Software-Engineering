def index_is_valid(ind, length):
    if ind in range(length):
        return True
    return False


pirate_ship_status = [int(i) for i in input().split(">")]
warship_status = [int(i) for i in input().split(">")]
max_health_for_section = int(input())

command = input()
have_a_winner = False

while not command == "Retire":

    if "Fire" in command:
        action = command.split()
        index = int(action[1])
        damage = int(action[2])
        if index_is_valid(index, len(warship_status)):
            warship_status[index] -= damage
            if warship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                have_a_winner = True
                break

    elif "Defend" in command:
        action = command.split()
        s_index = int(action[1])
        e_index = int(action[2])
        damage = int(action[3])
        if index_is_valid(s_index, len(pirate_ship_status)) and index_is_valid(e_index, len(pirate_ship_status)):
            for index in range(s_index, e_index + 1):
                pirate_ship_status[index] -= damage
            broken_sections = [i for i in pirate_ship_status if i <= 0]
            if broken_sections:
                print("You lost! The pirate ship has sunken.")
                have_a_winner = True
                break

    elif "Repair" in command:
        action = command.split()
        index = int(action[1])
        damage = int(action[2])
        if index_is_valid(index, len(pirate_ship_status)):
            pirate_ship_status[index] += damage
            if pirate_ship_status[index] > max_health_for_section:
                pirate_ship_status[index] = max_health_for_section

    elif command == "Status":
        section_to_repair = [i for i in pirate_ship_status if i < max_health_for_section * 0.2]
        print(f"{len(section_to_repair)} sections need repair.")

    command = input()

if not have_a_winner:
    print(f"Pirate ship status: {sum(pirate_ship_status)}")
    print(f"Warship status: {sum(warship_status)}")
