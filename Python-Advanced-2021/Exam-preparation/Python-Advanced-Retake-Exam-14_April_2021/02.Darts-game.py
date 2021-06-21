from collections import deque


players = deque(input().split(', '))
scores = {player: 501 for player in players}
board = [[el for el in input().split()] for _ in range(7)]
throws = 1
winner = None


while not winner:
    strike = input().split(', ')
    row = int(strike[0][1:])
    col = int(strike[1][:-1])
    current_player = players[0]
    throws += 1
    players.rotate()
    if not 0 <= row < len(board) or not 0 <= col < len(board):
        continue

    numeric_sum = int(board[row][0]) + int(board[row][-1]) + int(board[0][col]) + int(board[-1][col])
    hit = board[row][col]

    if hit.isdigit():
        scores[current_player] -= int(hit)
    elif hit == "B":
        winner = current_player
        break
    elif hit == "D":
        scores[current_player] -= numeric_sum * 2
    elif hit == "T":
        scores[current_player] -= numeric_sum * 3

    if scores[current_player] <= 0:
        winner = current_player
        break

print(f"{winner} won the game with {throws // 2} throws!")
