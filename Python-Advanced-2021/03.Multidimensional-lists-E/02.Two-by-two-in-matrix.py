rows, columns = map(int, input().split())
matrix = [[i for i in input().split()] for _ in range(rows)]

squares = 0

for row in range(rows - 1):
    for col in range(columns - 1):
        symbol = matrix[row][col]
        if symbol == matrix[row][col + 1] and symbol == matrix[row + 1][col] and symbol == matrix[row + 1][col + 1]:
            squares += 1

print(squares)
