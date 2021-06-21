from collections import deque


orders = deque(map(int, input().split(', ')))
employees_capacity = deque(map(int, input().split(', ')))
total_pizzas = 0
orders_completed = False
no_capacity = False


while True:
    if not orders:
        orders_completed = True
        break
    if not employees_capacity:
        no_capacity = True
        break
    if orders[0] > 10 or orders[0] <= 0:
        orders.popleft()
        continue
    if orders[0] <= employees_capacity[-1]:
        total_pizzas += orders.popleft()
        employees_capacity.pop()
        continue
    orders[0] -= employees_capacity[-1]
    total_pizzas += employees_capacity.pop()


if orders_completed:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join(map(str, employees_capacity))}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str, orders))}")
