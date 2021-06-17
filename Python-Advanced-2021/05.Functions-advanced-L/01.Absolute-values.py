def print_abs_values(numbers_as_list):
    absolutes = map(abs, numbers_as_list)
    return list(absolutes)


numbers = map(float, input().split())
print(print_abs_values(numbers))
