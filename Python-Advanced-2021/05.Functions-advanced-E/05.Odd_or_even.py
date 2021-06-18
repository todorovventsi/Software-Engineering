def odd_or_even(nums, command):
    nums_collection = filter(mapper[command], nums)
    return sum(nums_collection) * len(nums)


mapper = {
    "Odd": lambda x: x % 2 != 0,
    "Even": lambda x: x % 2 == 0
}

comm = input()
numbers = list(map(int, input().split()))
print(odd_or_even(numbers, comm))
