from collections import deque

kids = deque(input().split())
rotation = int(input())

while not len(kids) == 1:
    kids.rotate(-rotation)
    print(f"Removed {kids.pop()}")
print(f"Last is {kids.pop()}")
