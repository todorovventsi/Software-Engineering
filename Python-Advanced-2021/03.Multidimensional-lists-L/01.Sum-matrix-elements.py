rows, columns = map(int, input().split(", "))

matrix = []
matrix_total_sum = 0

for row in range(rows):
    read_row = [int(i) for i in input().split(", ")]
    matrix_total_sum += sum(read_row)
    matrix.append([])
    matrix[row].extend(read_row)

print(matrix_total_sum)
print(matrix)
