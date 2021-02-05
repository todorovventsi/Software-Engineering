def add_and_subtract(first, second, third):
    return subtract(sum_numbers(first, second), third)


def sum_numbers(first, second):
    return first + second


def subtract(added, third):
    return added - third


first_number = int(input())
second_number = int(input())
third_number = int(input())
result = add_and_subtract(first_number, second_number, third_number)
print(result)
