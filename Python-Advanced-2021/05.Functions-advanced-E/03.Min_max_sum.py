def evaluation(nums):
    print(f"The minimum number is {min(nums)}")
    print(f"The maximum number is {max(nums)}")
    print(f"The sum number is: {sum(nums)}")
    return


numbers = list(map(int, input().split()))
evaluation(numbers)
