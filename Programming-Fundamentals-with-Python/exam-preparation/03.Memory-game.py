board = input().split()

moves = 0

command = input()

while not command == "end":
    ind_one, ind_two = command.split()
    moves += 1
    ind_one_is_valid = True
    ind_two_is_valid = True
    if not (0 <= int(ind_one) < len(board)):
        ind_one_is_valid = False
    if not (0 <= int(ind_two) < len(board)):
        ind_two_is_valid = False
    if ind_one == ind_two or not ind_two_is_valid or not ind_one_is_valid:
        board.insert(int(len(board) / 2), f"-{moves}a")
        board.insert(int(len(board) / 2 + 1), f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
    elif board[int(ind_one)] == board[int(ind_two)]:
        print(f"Congrats! You have found matching elements - {board[int(ind_one)]}!")
        board = [i for i in board if not i == board[int(ind_one)]]
    elif not board[int(ind_one)] == board[int(ind_two)]:
        print("Try again!")
    if not board:
        print(f"You have won in {moves} turns!")
        break
    command = input()
if board:
    print("Sorry you lose :(")
    print(*board)
