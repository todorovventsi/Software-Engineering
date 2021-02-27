sugar_cubes = [int(i) for i in input().split()]

command = input()

while not command == "Mort":
    data = command.split()
    action = data[0]
    value = int(data[1])
    if action == "Add":
        sugar_cubes.append(value)
    elif action == "Remove":
        sugar_cubes.remove(value)
    elif action == "Replace":
        new_el = int(data[2])
        index = sugar_cubes.index(value)
        sugar_cubes[index] = new_el
    elif action == "Collapse":
        sugar_cubes = [x for x in sugar_cubes if x >= value]

    command = input()

print(*sugar_cubes)
