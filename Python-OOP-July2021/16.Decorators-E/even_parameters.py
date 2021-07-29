def is_even(num):
    if not isinstance(num, (int, float)):
        return False
    return num % 2 == 0


def even_parameters(func):
    def wrapper(*args):
        evens = [is_even(arg) for arg in args]
        if all(evens):
            return func(*args)
        return "Please use only even numbers!"

    return wrapper


@even_parameters
def add(a, b):
    return a + b


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(add(2, 4))
print(add("Peter", 1))
print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
