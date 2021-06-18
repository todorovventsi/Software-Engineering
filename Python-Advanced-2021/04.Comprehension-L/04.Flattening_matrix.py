rows = int(input())
matrix = [[int(num) for num in input().split(',')] for _ in range(rows)]

flat_matrix = []
[flat_matrix.extend(row) for row in matrix]

print(flat_matrix)
