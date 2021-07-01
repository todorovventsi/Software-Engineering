from game_core.constants import moves_mapper


def place_is_valid(num):
    return num in moves_mapper


def place_is_free(matrix, num):
    r = moves_mapper[num][0]
    c = moves_mapper[num][1]
    if matrix[r][c] == "X" or matrix[r][c] == "O":
        return False
    return True


def player_won(matrix: list, symbol_pl_1: str, symbol_pl_2: str):
    row_1 = [el for el in matrix[0]]
    row_2 = [el for el in matrix[1]]
    row_3 = [el for el in matrix[2]]
    col_1 = [row[0] for row in matrix]
    col_2 = [row[1] for row in matrix]
    col_3 = [row[2] for row in matrix]
    right_diagonal = [matrix[num][num] for num in range(3)]
    left_diagonal = [matrix[len(matrix) - num - 1][num] for num in range(2, -1, -1)]
    lines = [row_1, row_2, row_3, col_1, col_2, col_3, left_diagonal, right_diagonal]
    result = False
    for line in lines:
        check = [True if el == symbol_pl_1 else False for el in line]
        if all(check):
            result = True
            break
    return result


def no_more_moves(matrix):
    if " " in matrix[0] or " " in matrix[1] or " " in matrix[2]:
        return False
    return True
