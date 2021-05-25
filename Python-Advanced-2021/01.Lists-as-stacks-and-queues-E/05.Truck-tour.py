from collections import deque


total_petrol_pumps = int(input())

pumps_info = deque()
for number in range(0, total_petrol_pumps):
    fuel, distance = input().split()
    pumps_info.append([int(fuel), int(distance)])

success_point = None

for point in range(0, len(pumps_info)):
    current_fuel = 0
    is_complete = True
    for param in pumps_info:
        current_fuel += param[0]
        distance_to_next = param[1]
        if current_fuel < distance_to_next:
            is_complete = False
            break
        current_fuel -= distance_to_next
    if not is_complete:
        pumps_info.rotate(-1)
        continue
    else:
        success_point = point
        break

print(point)
