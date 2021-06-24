# Functions and move mapper:

def move_is_valid(coordinates):
    return True if 0 <= coordinates[0] < size and 0 <= coordinates[1] < size else False


move_mapper = {
    "up": lambda x, y: (x - 1, y),
    "down": lambda x, y: (x + 1, y),
    "right": lambda x, y: (x, y + 1),
    "left": lambda x, y: (x, y - 1),
}

# Inputs and statistics:

size = int(input())
field = [list(input()) for _ in range(size)]
snake_position = ()

for row in range(size):
    for col in range(size):
        if field[row][col] == "S":
            snake_position = (row, col)

food_eaten = 0
game_is_won = False

# Core logic

while True:
    command = input()
    next_location = move_mapper[command](snake_position[0], snake_position[1])
    if not move_is_valid(next_location):
        field[snake_position[0]][snake_position[1]] = "."
        print("Game over!")
        break
    location_host = field[next_location[0]][next_location[1]]
    if location_host == "*":
        food_eaten += 1
        field[snake_position[0]][snake_position[1]] = "."
        field[next_location[0]][next_location[1]] = "S"
        snake_position = next_location
    elif location_host == "B":
        field[snake_position[0]][snake_position[1]] = "."
        field[next_location[0]][next_location[1]] = "."
        b_location = ()
        for r in range(size):
            for c in range(size):
                if field[r][c] == "B":
                    b_location = (r, c)
                    break
        field[b_location[0]][b_location[1]] = "S"
        snake_position = b_location
    else:
        field[snake_position[0]][snake_position[1]] = "."
        field[next_location[0]][next_location[1]] = "S"
        snake_position = next_location
    if food_eaten >= 10:
        game_is_won = True
        break

# Outputs:

if game_is_won:
    print("You won! You fed the snake.")
print(f"Food eaten: {food_eaten}")
[print(''.join(row)) for row in field]
