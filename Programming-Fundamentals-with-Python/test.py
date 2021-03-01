def are_indices_different(ind1, ind2):
    if not ind1 == ind2:
        return True
    return False


def are_indices_in_range(sequence, ind1, ind2):
    if ind1 in range(len(sequence)) and ind2 in range(len(sequence)):
        return True
    return False


elements = input().split()

elements_indices = input()
moves = 0

while not elements_indices == "end":
    index1, index2 = [int(i) for i in elements_indices.split()]
    moves += 1
    if are_indices_different(index1, index2) and are_indices_in_range(elements, index1, index2):
        el1 = elements[index1]
        el2 = elements[index2]
        if el1 == el2:
            elements = [el for el in elements if not el == el1]
            print(f"Congrats! You have found matching elements - {el1}!")
        else:
            print("Try again!")
    else:
        half = len(elements) // 2
        elements.insert(half, f"-{moves}a")
        elements.insert(half, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
    if not elements:
        print(f"You have won in {moves} turns!")
        break

    elements_indices = input()

if elements:
    print("Sorry you lose :(")
    print(*elements)