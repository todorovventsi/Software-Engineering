def shoot(target, ind, power):



targets = [int(i) for i in input().split()]

action_command = input()

while not action_command == "End":
    action, index, value = action_command.split()

    action_command = input()