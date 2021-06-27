from collections import deque

chocolates = deque([int(i) for i in input().split(', ')])
milk = deque([int(i) for i in input().split(', ')])

milk_shakes = 0

while chocolates and milk:
    if milk_shakes >= 5:
        break
    current_choco = chocolates[-1]
    current_milk = milk[0]
    if current_choco <= 0:
        chocolates.pop()
        continue
    if current_milk <= 0:
        milk.popleft()
        continue
    if current_choco == current_milk:
        milk_shakes += 1
        chocolates.pop()
        milk.popleft()
        continue
    else:
        milk.rotate(-1)
        chocolates[-1] -= 5

print("Great! You made all the chocolate milkshakes needed!" if milk_shakes >= 5 else "Not enough milkshakes.")
print(f"Chocolate: {', '.join(map(str, chocolates))}" if chocolates else "Chocolate: empty")
print(f"Milk: {', '.join(map(str, milk))}" if milk else "Milk: empty")
