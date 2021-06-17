def round_numbers(nums):
    return list(map(round, nums))


numbers = map(float, input().split())
print(round_numbers(numbers))
