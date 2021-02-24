numbers = list(map(int, input().split(", ")))
zeros = numbers.count(0)
numbers = list(filter(lambda x: not x == 0, numbers))
# for _ in range(0, zeros):
#     numbers.append(0)
numbers.extend([0] * zeros)
print(numbers)
