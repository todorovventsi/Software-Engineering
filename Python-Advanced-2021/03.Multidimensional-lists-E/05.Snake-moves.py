rows, columns = map(int, input().split())
text = input()

symbol_id = 0
counter = 0
matrix = [[0 for _ in range(columns)] for _ in range(rows)]

for row in range(rows):

    if row % 2 == 0:
        for col in range(columns):
            matrix[row][col] = text[symbol_id]
            counter += 1
            symbol_id += 1
            if counter % len(text) == 0:
                symbol_id = 0
    else:
        for col in range(columns - 1, - 1, - 1):
            matrix[row][col] = text[symbol_id]
            counter += 1
            symbol_id += 1
            if counter % len(text) == 0:
                symbol_id = 0

for row in matrix:
    print("".join(row))
