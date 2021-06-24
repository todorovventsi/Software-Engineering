from math import floor

n = int(input())
field = [input().split() for _ in range(n)]
player_pos = [0, 0]
movement = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}
path = []
coins = 0


def game_over(c):

    if c > 0:
        c /= 2

    print(f"Game over! You've collected {floor(c)} coins.")
    print("Your path:")
    [print(p) for p in path]


for row in range(n):
    for col in range(n):
        if field[row][col] == "P":
            player_pos = [row, col]

while True:
    command = input()
    row, col = player_pos
    if command in movement:
        row += movement[command][0]
        col += movement[command][1]
    else:
        continue

    if not (0 <= row < n and 0 <= col < n):
        game_over(coins)
        break
    current_pos = field[row][col]
    if current_pos.isdigit():
        coins += int(current_pos)
    elif current_pos == "X":
        game_over(coins)
        break
    player_pos = [row, col]
    path.append([row, col])
    if coins >= 100:
        print(f"You won! You've collected {coins} coins.")
        print("Your path:")
        [print(p) for p in path]
        break

