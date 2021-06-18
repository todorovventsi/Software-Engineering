def filter_evens(nums):
    evens = filter(lambda x: x % 2 == 0, nums)
    return list(evens)


numbers = map(int, input().split())
print(filter_evens(numbers))
