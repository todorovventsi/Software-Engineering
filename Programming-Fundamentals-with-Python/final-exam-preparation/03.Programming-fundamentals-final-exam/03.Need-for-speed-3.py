n_cars = int(input())

cars_collection = {}

for _ in range(n_cars):
    car_name, mileage, fuel = input().split("|")
    car_mileage = int(mileage)
    car_fuel = int(fuel)
    cars_collection[car_name] = {"mileage": car_mileage, "fuel": car_fuel}

command = input()
while not command == "Stop":
    data = command.split(" : ")
    car = data[1]
    if "Drive" in data:
        distance = int(data[2])
        fuel_needed = int(data[3])
        if cars_collection[car]["fuel"] < fuel_needed:
            print("Not enough fuel to make that ride")
            command = input()
            continue
        cars_collection[car]["mileage"] += distance
        cars_collection[car]["fuel"] -= fuel_needed
        print(f"{car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")
        if cars_collection[car]["mileage"] >= 100000:
            cars_collection.pop(car)
            print(f"Time to sell the {car}!")
    elif "Refuel" in data:
        fuel_to_add = int(data[2])
        current_fuel = cars_collection[car]["fuel"]
        if fuel_to_add + current_fuel > 75:
            cars_collection[car]["fuel"] = 75
        else:
            cars_collection[car]["fuel"] += fuel_to_add
        added = cars_collection[car]["fuel"] - current_fuel
        print(f"{car} refueled with {added} liters")
    elif "Revert" in data:
        kilometers = int(data[2])
        cars_collection[car]["mileage"] -= kilometers
        if cars_collection[car]["mileage"] < 10000:
            cars_collection[car]["mileage"] = 10000
            command = input()
            continue
        print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

cars_collection = sorted(cars_collection.items(), key=lambda kvp: (-kvp[1]["mileage"], kvp[0][0]))
for car in cars_collection:
    name = car[0]
    mileage = car[1]["mileage"]
    fuel = car[1]["fuel"]
    print(f"{name} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")
