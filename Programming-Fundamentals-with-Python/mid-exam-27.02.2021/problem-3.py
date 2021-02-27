cards_arsenal = input().split(":")
attack_cards = []

command = input()

while not command == "Ready":
    data = command.split()
    action = data[0]

    if action == "Add":
        to_add = data[1]
        if to_add in cards_arsenal:
            attack_cards.append(to_add)
        else:
            print("Card not found.")

    elif action == "Insert":
        to_insert = data[1]
        index = int(data[2])
        if to_insert not in cards_arsenal or index not in range(len(attack_cards)):
            print("Error!")
        else:
            attack_cards.insert(index, to_insert)

    elif action == "Remove":
        to_remove = data[1]
        if to_remove in attack_cards:
            attack_cards.remove(to_remove)
        else:
            print("Card not found.")

    elif action == "Swap":
        swap_one = data[1]
        swap_two = data[2]
        ind_one = attack_cards.index(swap_one)
        ind_two = attack_cards.index(swap_two)
        attack_cards[ind_one], attack_cards[ind_two] = attack_cards[ind_two], attack_cards[ind_one]

    elif "Shuffle deck" in command:
        attack_cards = attack_cards[::-1]

    command = input()

print(*attack_cards)
