import sys


def define_sub_matrix(grid, sub_size, initial_index):
    '''

    :param grid: a matrix from which a sub matrix will be extracted
    :param sub_size: the size of the sub matrix
    :param initial_index: the position of the first element of the parent matrix
    :return: a square sub matrix extracted from the parent matrix with the given matrix size
    '''
    r, c = initial_index
    result = []
    for _ in range(sub_size):
        current_row = grid[r][c:c + sub_size]
        result.append(current_row)
        r += 1
    return result


rows, columns = map(int, input().split())
sub_matrix_size = 3
matrix = [[int(i) for i in input().split()] for _ in range(rows)]
biggest_submatrix_value = -sys.maxsize
biggest_submatrix = None
for row in range(rows - sub_matrix_size + 1):
    for col in range(columns - sub_matrix_size + 1):
        current_sub_matrix = define_sub_matrix(matrix, sub_matrix_size, (row, col))
        list_of_rows_sum = [sum(row) for row in current_sub_matrix]
        current_sum = sum(list_of_rows_sum)
        if current_sum > biggest_submatrix_value:
            biggest_submatrix_value = current_sum
            biggest_submatrix = current_sub_matrix

print(f"Sum = {biggest_submatrix_value}")
[print(*row) for row in biggest_submatrix]
