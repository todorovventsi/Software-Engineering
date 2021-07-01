from random import choice
from collections import deque

from game_core.validations import player_won, place_is_valid, place_is_free, no_more_moves
from game_core.constants import moves_mapper


def play(player_1, player_2):
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    # who to start random player
    first_to_start = choice([player_1, player_2])

    # populate deque with starting player on index 0
    if first_to_start is player_1:
        players = deque([player_1, player_2])
    else:
        players = deque([player_2, player_1])

    # Announce who starts first
    print(f"{players[0].name} starts first!")

    while True:
        # starting player choose where to place a sign while he choose a valid number
        player_choice = int(input(f"{players[0].name} choose a free position [1-9]: "))
        while not place_is_valid(player_choice) or not place_is_free(board, player_choice):
            player_choice = int(input(f"{players[0].name} choose a free position [1-9]: "))

        # place player's sign on position and print board
        board[moves_mapper[player_choice][0]][moves_mapper[player_choice][1]] = players[0].sign
        [print(*row, sep="|") for row in board]

        # check if player is a winner and if so stop the game
        if player_won(board, players[0].sign, players[1].sign):
            print(f"{players[0].name} won the game")
            break

        # check if there are any places to move and if there arent stop the game without a winner
        if no_more_moves(board):
            print("Game end without a winner!")
            break

        # if the game continue rotate the deque and go on
        players.rotate()
