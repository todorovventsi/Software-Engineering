n = int(input())

positive = []
negative = []

for _ in range(n):
    number = int(input())
    if number < 0:
        negative.append(number)
    else:
        positive.append(number)
print(positive)
print(negative)
print(f"Count of positives: {len(positive)}. Sum of negatives: {sum(negative)}")
