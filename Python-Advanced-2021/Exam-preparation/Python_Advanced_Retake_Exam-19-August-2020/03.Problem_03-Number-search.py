def numbers_searching(*args):
    sequence = [num for num in args]
    sequence.sort()
    duplicates = {num for num in sequence if sequence.count(num) > 1}
    duplicates_l = list(duplicates)
    duplicates_l.sort()
    no_duplicates = set(sequence)
    comparison = {num for num in range(sequence[0], sequence[-1] + 1)}
    missing_value = comparison.difference(no_duplicates)
    result = [*missing_value, duplicates_l]
    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
