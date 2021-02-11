numbers = list(map(int, input().split(", ")))
evens_indices = [index for index, num in enumerate(numbers) if num % 2 == 0]
print(evens_indices)