def even_odd(*args):
    numbers = map(int, args[:-1])
    command = args[-1]
    result = filter(mapper[command], numbers)
    return list(result)


mapper = {
    "even": lambda x: x % 2 == 0,
    "odd": lambda x: not x % 2 == 0
}

print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
