def range_is_valid(*args):
    return True if 0 <= args[0] < 5 and 0 <= args[1] < 5 else False


move_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

field = [input().split() for _ in range(5)]
number_of_commands = int(input())
position = []
for row in range(5):
    for col in range(5):
        if field[row][col] == "A":
            position.extend([row, col])

shot_targets = []
targets_left = 0

for _ in range(number_of_commands):
    command = input().split()
    r, c = position
    if command[0] == "move":
        direction = command[1]
        steps = int(command[2])
        next_row = r + move_mapper[direction][0] * steps
        next_col = c + move_mapper[direction][1] * steps
        if range_is_valid(next_row, next_col):
            if field[next_row][next_col] == ".":
                field[position[0]][position[1]] = "."
                position[0] = next_row
                position[1] = next_col
                field[next_row][next_col] = "A"
    elif command[0] == "shoot":
        direction = command[1]
        next_r = position[0] + move_mapper[direction][0]
        next_c = position[1] + move_mapper[direction][1]
        while range_is_valid(next_r, next_c):
            if field[next_r][next_c] == "x":
                shot_targets.append([next_r, next_c])
                field[next_r][next_c] = "."
                break
            next_r += move_mapper[direction][0]
            next_c += move_mapper[direction][1]


for row in range(5):
    for col in range(5):
        if field[row][col] == "x":
            targets_left += 1

print(f"Training completed! All {len(shot_targets)} targets hit." if not targets_left else f"Training not completed! {targets_left} targets left.")
[print(target) for target in shot_targets]
