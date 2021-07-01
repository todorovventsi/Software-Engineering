from game_core.setup import Player
from game_core.constants import board_numeration
from game_core.logic import play


# Setup initial conditions
def start_game():
    player_one = Player(input("Player one name: "))
    player_two = Player(input("Player two name: "))

    player_one.sign = input(f"{player_one.name}, would you like to play with 'X' or 'O'?").upper()
    while player_one.sign not in ["X", "O"]:
        player_one.sign = input(f"{player_one.name}, would you like to play with 'X' or 'O'?").upper()
    player_two.sign = "X" if player_one.sign == "O" else "O"
    [print(*row) for row in board_numeration]
    play(player_one, player_two)


# Starting point
if __name__ == '__main__':
    start_game()

