matrix_size = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(matrix_size)]

primary_diagonal = 0
secondary_diagonal = 0

for row in range(matrix_size):
    primary_diagonal += matrix[row][row]
    secondary_diagonal += matrix[row][matrix_size - row - 1]

print(abs(primary_diagonal - secondary_diagonal))
