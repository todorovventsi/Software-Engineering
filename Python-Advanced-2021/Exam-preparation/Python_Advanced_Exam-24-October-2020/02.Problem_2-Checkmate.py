def range_is_valid(r, c, n = 8):
    return True if 0 <= r < n and 0 <= c < n else False


moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
    "up_right": (-1, 1),
    "up_left": (-1, -1),
    "down_right": (1, 1),
    "down_left": (1, -1),
}

n = 8
board = [input().split() for _ in range(n)]
active_queens = []

for row in range(len(board)):
    for col in range(len(board)):
        if board[row][col] == "Q":
            for direction in moves:
                next_row = row + moves[direction][0]
                next_col = col + moves[direction][1]
                while range_is_valid(next_row, next_col):
                    if board[next_row][next_col] == "Q":
                        break
                    if board[next_row][next_col] == "K":
                        active_queens.append([row, col])
                        break
                    next_row += moves[direction][0]
                    next_col += moves[direction][1]

if active_queens:
    print(*active_queens, sep="\n")
else:
    print("The king is safe!")
