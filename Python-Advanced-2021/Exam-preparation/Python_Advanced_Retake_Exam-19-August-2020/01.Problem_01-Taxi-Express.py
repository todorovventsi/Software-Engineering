from collections import deque


customers = deque([int(i) for i in input().split(', ')])
taxis = deque([int(i) for i in input().split(', ')])

total_time = 0

while customers and taxis:
    customer = customers[0]
    taxi = taxis.pop()
    if taxi >= customer:
        total_time += customers.popleft()


if customers:
    print(f"Not all customers were driven to their destinations\nCustomers left: {', '.join(map(str, customers))}")
else:
    print(f"All customers were driven to their destinations\nTotal time: {total_time} minutes")
