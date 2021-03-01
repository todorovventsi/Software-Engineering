def get_factorial(x):
    result = 1
    for i in range(x, 0, - 1):
        result *= i
    return result


def factorial_division(a, b):
    result = a / b
    return result


number_one = int(input())
number_two = int(input())

f_number_one = get_factorial(number_one)
f_number_two = get_factorial(number_two)
output = factorial_division(f_number_one, f_number_two)
print(f"{output:.2f}")
