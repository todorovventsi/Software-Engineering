import sys

rows, columns = map(int, input().split(", "))
matrix = [[int(i) for i in input().split(", ")] for _ in range(rows)]

max_square_sum = -sys.maxsize
reference_index = None

for row in range(rows - 1, 0, -1):
    for column in range(columns - 1, 0, -1):
        current_sum = matrix[row][column] + matrix[row][column - 1] \
                      + matrix[row - 1][column] + matrix[row - 1][column - 1]
        if current_sum >= max_square_sum:
            max_square_sum = current_sum
            reference_index = (row, column)

row, col = reference_index
print(matrix[row - 1][col - 1], matrix[row - 1][col])
print(matrix[row][col - 1], matrix[row][col])
print(max_square_sum)
