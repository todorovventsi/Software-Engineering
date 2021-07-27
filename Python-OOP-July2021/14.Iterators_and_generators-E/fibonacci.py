def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        b += a
        yield b
        a += b


generator = fibonacci()
for i in range(5):
    print(next(generator))
