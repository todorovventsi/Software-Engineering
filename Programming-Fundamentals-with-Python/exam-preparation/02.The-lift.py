people_waiting = int(input())
lift_wagons = list(map(int, input().split()))

for index, wagon in enumerate(lift_wagons):
    free_space = 4 - wagon
    if free_space == 0:
        continue
    if people_waiting >= 4:
        lift_wagons[index] += free_space
        people_waiting -= free_space
    else:
        lift_wagons[index] += people_waiting
        people_waiting -= people_waiting
if people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
elif people_waiting == 0 and not lift_wagons[-1] == 4:
    print("The lift has empty spots!")
print(*lift_wagons)
