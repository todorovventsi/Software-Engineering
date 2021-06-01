matrix_size = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(matrix_size)]

diagonal_value = 0

for row in range(matrix_size):
    diagonal_value += matrix[row][row]
print(diagonal_value)
