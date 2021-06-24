def move_is_valid(coordinates):
    return True if 0 <= coordinates[0] < size and 0 <= coordinates[1] < size else False


moves_mapper = {
    "up": lambda x, y: (x - 1, y),
    "down": lambda x, y: (x + 1, y),
    "right": lambda x, y: (x, y + 1),
    "left": lambda x, y: (x, y - 1),
}

initial_string = input()
size = int(input())
field = [list(input()) for _ in range(size)]
number_of_moves = int(input())

player_position = ()
for row in range(size):
    for col in range(size):
        if field[row][col] == "P":
            player_position = (row, col)

for _ in range(number_of_moves):
    command = input()
    next_position = moves_mapper[command](*player_position)
    if not move_is_valid(next_position):
        initial_string = initial_string[0:-1]
        continue
    field[player_position[0]][player_position[1]] = "-"
    location_symbol = field[next_position[0]][next_position[1]]
    if not location_symbol == "-":
        initial_string += location_symbol
        field[next_position[0]][next_position[1]] = "P"
        player_position = next_position
    else:
        field[next_position[0]][next_position[1]] = "P"
        player_position = next_position

print(initial_string)
[print(f"{''.join(row)}") for row in field]
