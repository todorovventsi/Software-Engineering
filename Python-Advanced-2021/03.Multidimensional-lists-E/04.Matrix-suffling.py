def swap_positions(grid, r_1, c_1, r_2, c_2):
    grid[r_1][c_1], grid[r_2][c_2] = grid[r_2][c_2], grid[r_1][c_1]
    return


rows, columns = map(int, input().split())
matrix = [[i for i in input().split()] for _ in range(rows)]

command = input()
while not command == "END":
    try:
        data, row_1, col_1, row_2, col_2 = command.split()
        swap_positions(matrix, int(row_1), int(col_1), int(row_2), int(col_2))
        [print(*row) for row in matrix]
    except:
        print("Invalid input!")

    command = input()
