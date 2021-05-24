from collections import deque

prepared_food = int(input())
costumer_orders = deque([int(i) for i in input().split()])

print(max(costumer_orders))
while True:
    if not costumer_orders:
        print("Orders complete")
        break
    if prepared_food >= costumer_orders[0]:
        next_in_line_order = costumer_orders.popleft()
        prepared_food -= next_in_line_order
        continue
    if prepared_food < costumer_orders[0]:
        print(f"Orders left:", end=" ")
        for _ in range(len(costumer_orders)):
            print(costumer_orders.popleft(), end=" ")
        break
