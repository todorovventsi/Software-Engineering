first_length, second_length = input().split()
first_set = set(input() for _ in range(int(first_length)))
second_set = set(input() for _ in range(int(second_length)))

print(*first_set.intersection(second_set), sep="\n")
