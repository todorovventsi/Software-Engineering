# all_numbers = [int(num) for num in input().split(", ")]
all_numbers = list(map(lambda x: int(x), input().split(", ")))

group = 10
while all_numbers:
    current_group = [num for num in all_numbers if num <= group]
    for num in current_group:
        all_numbers.remove(num)
    print(f"Group of {group}'s: {current_group}")
    group += 10
