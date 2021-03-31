how_many = int(input())
my_cars = {}
for _ in range(how_many):
    car = input().split("|")
    my_cars[car[0]] = [int(car[1]), int(car[2])]
# {'Audi A6': ('38000', '62'), 'Mercedes CLS': ('11000', '35'), 'Volkswagen Passat CC': ('45678', '5')}
data = input()
while not data == "Stop":
    command = data.split(" : ")
    action = command[0]
    if action == "Drive":
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        if my_cars[car][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            my_cars[car][0] += distance
            my_cars[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if my_cars[car][0] >= 100000:
            my_cars.pop(car)
            print(f"Time to sell the {car}!")
    elif action == "Refuel":
        car = command[1]
        fuel = int(command[2])
        initial_fuel = my_cars[car][1]
        my_cars[car][1] += fuel
        if my_cars[car][1] < 75:
            print(f"{car} refueled with {fuel} liters")
        else:
            my_cars[car][1] = 75
            added_fuel = my_cars[car][1] - initial_fuel
            print(f"{car} refueled with {added_fuel} liters")
    elif action == "Revert":
        car = command[1]
        kilometers = int(command[2])
        my_cars[car][0] -= kilometers
        if my_cars[car][0] >= 10000:
            print(f"{car} mileage decreased by {kilometers} kilometers")
        else:
            my_cars[car][0] = 10000
    data = input()
my_cars = dict(sorted(my_cars.items(), key=lambda kvp: (- kvp[1][0], kvp[0])))
for car in my_cars:
    print(f"{car} -> Mileage: {my_cars[car][0]} kms, Fuel in the tank: {my_cars[car][1]} lt.")