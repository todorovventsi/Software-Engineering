numbers = list(map(int, input().split()))

command = input()

while not command == "end":
    current_command = command.split()
    if "swap" in current_command:
        numbers[int(current_command[1])], numbers[int(current_command[2])] = numbers[int(current_command[2])], numbers[int(current_command[1])]
    elif "multiply" in current_command:
        product = numbers[int(current_command[1])] * numbers[int(current_command[2])]
        numbers[int(current_command[1])] = product
    elif "decrease" in current_command:
        numbers = list(map(lambda x: x - 1, numbers))

    command = input()

print(*numbers, sep=", ")
