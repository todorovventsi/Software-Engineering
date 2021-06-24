# Imports

from collections import deque

# Inputs and statistics

males = deque([int(i) for i in input().split()])
females = deque([int(i) for i in input().split()])
matches = 0

# Core logic

while males and females:
    if males[-1] <= 0:
        males.pop()
        continue
    if females[0] <= 0:
        females.popleft()
        continue
    if males[-1] % 25 == 0:
        males.pop()
        males.pop()
        continue
    if females[0] % 25 == 0:
        females.popleft()
        females.popleft()
        continue
    if males[-1] == females[0]:
        matches += 1
        males.pop()
        females.popleft()
    else:
        males[-1] -= 2
        females.popleft()

# Outputs
males.reverse()
print(f"Matches: {matches}")
print("Males left: none" if not males else f"Males left: {', '.join(map(str, males))}")
print("Females left: none" if not females else f"Females left: {', '.join(map(str, females))}")
