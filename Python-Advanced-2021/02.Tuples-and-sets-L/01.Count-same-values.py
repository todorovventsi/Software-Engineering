sequence_of_values = list(map(float, input().split()))

values_count = {}
for value in sequence_of_values:
    if value not in values_count:
        values_count[value] = sequence_of_values.count(value)
[print(f"{key} - {value} times") for key, value in values_count.items()]
