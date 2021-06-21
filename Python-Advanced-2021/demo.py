# def recursive_power(number, power):
#     if power == 0:
#         return 1
#     return number * recursive_power(number, power - 1)
#
# print(recursive_power(2, 4))

def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)


print(factorial(4))
