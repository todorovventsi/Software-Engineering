def list_manipulator(*args):
    list_of_nums = args[0]
    command = '-'.join([args[1], args[2]])
    numbers = args[3:]
    return command_mapper[command](list_of_nums, numbers)


def add_beginning(l_nums, nums):
    result = []
    result.extend(nums)
    result.extend(l_nums)
    return result


def add_end(l_nums, nums):
    result = []
    result.extend(l_nums)
    result.extend(nums)
    return result


def remove_beginning(l_nums, nums):
    if not nums:
        return l_nums[1:]
    return l_nums[nums[0]:]


def remove_end(l_nums, nums):
    if not nums:
        return l_nums[0:-1]
    return l_nums[0:-nums[0]]


command_mapper = {
    "add-beginning": add_beginning,
    "add-end": add_end,
    "remove-beginning": remove_beginning,
    "remove-end": remove_end
}


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
