from collections import deque

clothes_delivery = deque([int(i) for i in input().split()])
rack_capacity = int(input())

used_racks = 0

while clothes_delivery:
    current_usage = 0
    try:
        while (current_usage + clothes_delivery[-1]) <= rack_capacity:
            current_usage += clothes_delivery.pop()
        used_racks += 1
    except:
        used_racks += 1
print(used_racks)
