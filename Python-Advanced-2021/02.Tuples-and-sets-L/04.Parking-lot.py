number_of_operations = int(input())

parking_register = set()

for _ in range(number_of_operations):
    direction, car_plate = input().split(", ")
    if direction == "IN":
        parking_register.add(car_plate)
        continue
    if parking_register:
        parking_register.discard(car_plate)

if parking_register:
    print(*parking_register, sep="\n")
else:
    print("Parking Lot is Empty")
