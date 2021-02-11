number_of_wagons = int(input())
wagons = [0 for i in range(number_of_wagons)]

command = input().split()
while "End" not in command:
    if "add" in command:
        wagons[-1] += int(command[1])
    elif "insert" in command:
        wagons[int(command[1])] += int(command[-1])
    elif "leave" in command:
        wagons[int(command[1])] -= int(command[-1])
    command = input().split()

print(wagons)
