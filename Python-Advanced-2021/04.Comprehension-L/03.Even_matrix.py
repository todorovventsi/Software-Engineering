rows = int(input())
matrix = [[int(num) for num in input().split(', ') if int(num) % 2 == 0] for _ in range(rows)]
print(matrix)
