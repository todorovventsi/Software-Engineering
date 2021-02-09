import math


def distance_to_origin(x, y):
    return abs(math.sqrt(x ** 2 + y ** 2))


def distance_between_points(x_first, y_first, x_second, y_second):
    distance = math.sqrt((abs(x_first) - abs(x_second))**2 + (abs(y_first) - abs(y_second))**2)
    return distance


coordinates = []
for _ in range(8):
    coordinates.append(float(input()))

first_line = distance_between_points(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
second_line = distance_between_points(coordinates[4], coordinates[5], coordinates[6], coordinates[7])

first_point_distance = distance_to_origin(coordinates[0], coordinates[1])
second_point_distance = distance_to_origin(coordinates[2], coordinates[3])
third_point_distance = distance_to_origin(coordinates[4], coordinates[5])
fourth_point_distance = distance_to_origin(coordinates[6], coordinates[7])

if first_line > second_line or not abs(first_line - second_line) <= 1*10**(-8):
    if first_point_distance < second_point_distance:
        print(f"({math.floor(coordinates[0])}, {math.floor(coordinates[1])})({math.floor(coordinates[2])}, {math.floor(coordinates[3])})")
    else:
        print(f"({math.floor(coordinates[2])}, {math.floor(coordinates[3])})({math.floor(coordinates[0])}, {math.floor(coordinates[1])})")
else:
    if third_point_distance < fourth_point_distance:
        print(f"({math.floor(coordinates[4])}, {math.floor(coordinates[5])})({math.floor(coordinates[6])}, {math.floor(coordinates[7])})")
    else:
        print(f"({math.floor(coordinates[6])}, {math.floor(coordinates[7])})({math.floor(coordinates[4])}, {math.floor(coordinates[5])})")
