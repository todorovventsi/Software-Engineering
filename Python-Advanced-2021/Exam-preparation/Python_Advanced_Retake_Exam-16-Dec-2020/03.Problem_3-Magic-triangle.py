def get_magic_triangle(n):
    result = [[1], [1, 1]]
    for row in range(3, n + 1):
        previous_row = result[row - 2]
        current = []
        for index in range(0, row):
            if index == 0 or index == row - 1:
                current.append(1)
            else:
                value = previous_row[index - 1] + previous_row[index]
                current.append(value)
        result.append(current)
    return result


get_magic_triangle(5)
