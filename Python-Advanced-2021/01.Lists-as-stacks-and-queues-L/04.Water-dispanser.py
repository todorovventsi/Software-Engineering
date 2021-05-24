from collections import deque

dispanser_queue = deque()
water_available = int(input())
while True:
    name = input()
    if name == "Start":
        break
    dispanser_queue.append(name)


command = input()
while not command == "End":
    if "refill" in command:
        liters = int(command.split()[1])
        water_available += liters
    else:
        liters = int(command)
        if liters <= water_available:
            water_available -= liters
            print(f"{dispanser_queue.popleft()} got water")
        else:
            print(f"{dispanser_queue.popleft()} must wait")

    command = input()
print(f"{water_available} liters left")
