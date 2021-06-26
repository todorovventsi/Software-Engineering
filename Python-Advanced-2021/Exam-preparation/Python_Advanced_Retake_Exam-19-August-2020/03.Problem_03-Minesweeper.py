def index_is_valid(*args):
    return True if 0 <= args[0] < args[2] and 0 <= args[1] < args[2] else False


moves_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "up_right": (-1, 1),
    "up_left": (-1, -1),
    "down_right": (1, 1),
    "down_left": (1, -1),
}

field_size = int(input())
bombs_number = int(input())
field = [[0 for _ in range(field_size)] for _ in range(field_size)]

for _ in range(bombs_number):
    coordinates = map(int, input().strip("()").split(", "))
    y, x = coordinates
    field[y][x] = "*"

for row in range(field_size):
    for col in range(field_size):
        if not field[row][col] == "*":
            for direction in moves_mapper:
                next_r = row + moves_mapper[direction][0]
                next_c = col + moves_mapper[direction][1]
                if index_is_valid(next_r, next_c, field_size):
                    if field[next_r][next_c] == "*":
                        field[row][col] += 1

[print(f"{' '.join(map(str, row))}") for row in field]
