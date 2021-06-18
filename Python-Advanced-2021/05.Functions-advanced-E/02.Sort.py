def sorting_int_nums(nums):
    sotred_collection = sorted(nums)
    return list(sotred_collection)


numbers = map(int, input().split())
print(sorting_int_nums(numbers))
