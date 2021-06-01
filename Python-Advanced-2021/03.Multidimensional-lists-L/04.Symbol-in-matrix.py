matrix_size = int(input())
matrix = [[i for i in list(input())] for _ in range(matrix_size)]
searched_symbol = input()

position = None

for row in range(matrix_size):
    for column in range(matrix_size):
        if matrix[row][column] == searched_symbol:
            position = (row, column)
            break
    if position:
        break

print(position if position else f"{searched_symbol} does not occur in the matrix")
