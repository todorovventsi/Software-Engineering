# d = sqrt(a**2 + b**2)
import math


def distance_to_origin(x, y):
    return abs(math.sqrt(x**2 + y**2))


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

d_first = distance_to_origin(x1, y1)
d_second = distance_to_origin(x2, y2)

if d_first <= d_second:
    print(f"({math.floor(x1)}, {math.floor(y1)})")
else:
    print(f"({math.floor(x2)}, {math.floor(y2)})")
