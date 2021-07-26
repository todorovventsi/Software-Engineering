def squares(num):
    value = 1
    while value <= num:
        yield value ** 2
        value += 1


print(list(squares(5)))
