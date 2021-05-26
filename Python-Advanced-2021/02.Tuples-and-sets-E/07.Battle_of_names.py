lines = int(input())

odd_values = set()
even_values = set()

for line in range(1, lines + 1):
    name = input()
    ascii_values = sum(ord(char) for char in name)
    name_score = int(ascii_values / line)
    if name_score % 2 == 0:
        even_values.add(name_score)
        continue
    odd_values.add(name_score)

if sum(odd_values) == sum(even_values):
    print(*odd_values.union(even_values), sep=", ")
elif sum(odd_values) > sum(even_values):
    print(*odd_values.difference(even_values), sep=", ")
else:
    print(*odd_values.symmetric_difference(even_values), sep=", ")
