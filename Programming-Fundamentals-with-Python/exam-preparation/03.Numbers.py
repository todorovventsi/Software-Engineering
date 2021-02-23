from statistics import mean


numbers = list(map(int, input().split()))

average = mean(numbers)

greater_than_avg = list(filter(lambda x: x > average, numbers))
greater_than_avg.sort(reverse=True)
while len(greater_than_avg) > 5:
    greater_than_avg.pop()
if greater_than_avg:
    print(*greater_than_avg)
else:
    print("No")
