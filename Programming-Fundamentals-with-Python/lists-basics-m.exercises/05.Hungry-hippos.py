def if_current_has_neighbors(r, c):
    counter = 0
    checked = []
    neighbors = []


n_rows = int(input())

game_field = [[int(i) for i in input().split()] for _ in range(n_rows)]
n_columns = len(game_field[0])
result = []

for row in range(n_rows):
    for col in range(n_columns):
        cc_result = if_current_has_neighbors(row, col)
        result.append(cc_result)

print(result)


