from collections import deque


def best_list_pureness(*args):
    numbers, rotations = args
    record = {}
    nums = deque(numbers)
    for rotation in range(0, rotations + 1):
        result = sum([number * index for number, index in enumerate(nums)])
        record[rotation] = result
        nums.rotate()
    record = sorted(record.items(), key=lambda x: (-x[1], x[0]))
    return f"Best pureness {record[0][1]} after {record[0][0]} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)