# Functions to check results:
def game_ends(result):
    return int(result * 0.5)


def valid_move(pos):
    r = pos[0]
    c = pos[1]
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


# Moves mapper

moves_mapper = {
    "up": lambda x, y: (x - 1, y),
    "down": lambda x, y: (x + 1, y),
    "right": lambda x, y: (x, y + 1),
    "left": lambda x, y: (x, y - 1),
}


# Inputs and field creation

size = int(input())
field = [[el for el in input().split()] for _ in range(size)]
path = []
coins = 0
position = ()
game_is_won = False

for row in range(size):
    for col in range(size):
        if field[row][col] == "P":
            position = (row, col)


while True:
    command = input()
    if command not in moves_mapper:
        continue
    next_position = moves_mapper[command](position[0], position[1])
    if valid_move(next_position):
        collect = field[next_position[0]][next_position[1]]
        if collect == "X":
            coins = game_ends(coins)
            break
        path.append(list(next_position))
        position = next_position
        coins += int(collect)
        if coins >= 100:
            game_is_won = True
            break
        continue
    coins = game_ends(coins)
    break

print(f"You won! You've collected {coins} coins." if game_is_won else f"Game over! You've collected {coins} coins.")
print("Your path:")
print(*path, sep="\n")
