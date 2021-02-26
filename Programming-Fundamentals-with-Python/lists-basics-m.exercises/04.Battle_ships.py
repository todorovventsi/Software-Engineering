rows_of_ships = int(input())

ships_structure = [[int(i) for i in input().split()] for _ in range(rows_of_ships)]
attacks = input().split()
destroyed_ships = 0
for attack in attacks:
    coordinates = attack.split("-")
    row = int(coordinates[0])
    col = int(coordinates[1])
    if ships_structure[row][col] > 0:
        ships_structure[row][col] -= 1
        if ships_structure[row][col] == 0:
            destroyed_ships += 1

print(destroyed_ships)
