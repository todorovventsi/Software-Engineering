targets = [int(i) for i in input().split()]

command = input()

while not command == "End":
    action, t_index, power = command.split()
    target_exist = True
    if not 0 <= int(t_index) < len(targets):
        target_exist = False
    if action == "Shoot" and target_exist:
        targets[int(t_index)] -= int(power)
        if targets[int(t_index)] <= 0:
            targets.pop(int(t_index))
    elif action == "Add":
        if target_exist:
            targets.insert(int(t_index), int(power))
        else:
            print("Invalid placement!")
    elif action == "Strike":
        if target_exist and (int(t_index) + int(power) < len(targets)) and (0 <= int(t_index) - int(power)):
            to_remove = set()
            for ind in range(0, int(power) + 1):
                to_remove.add(targets[int(t_index) + ind])
                to_remove.add(targets[int(t_index) - ind])
            for item in to_remove:
                targets.remove(int(item))
        else:
            print("Strike missed!")
    command = input()

print(*targets, sep="|")
