from collections import deque


def remove_both(collection_one, collection_two):
    collection_one.popleft()
    collection_two.pop()


firework_effects = deque([int(el) for el in input().split(', ')])
explosive_power = deque([int(el) for el in input().split(', ')])

fireworks = {"palm": 0, "willow": 0, "crossette": 0}
success = False

while True:
    if not firework_effects or not explosive_power:
        break
    firework, power = firework_effects[0], explosive_power[-1]
    if firework <= 0:
        firework_effects.popleft()
        continue
    if power <= 0:
        explosive_power.pop()
        continue

    value = firework + power
    if value % 3 == 0 and not value % 5 == 0:
        fireworks["palm"] += 1
        remove_both(firework_effects, explosive_power)
    elif value % 5 == 0 and not value % 3 == 0:
        fireworks["willow"] += 1
        remove_both(firework_effects, explosive_power)
    elif value % 3 == 0 and value % 5 == 0:
        fireworks["crossette"] += 1
        remove_both(firework_effects, explosive_power)
    else:
        firework_effects[0] -= 1
        firework_effects.rotate(-1)
        continue

    if fireworks["palm"] >= 3 and fireworks["willow"] >= 3 and fireworks["crossette"] >= 3:
        success = True
        break

print("Congrats! You made the perfect firework show!" if success else "Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")
print(f"Palm Fireworks: {fireworks['palm']}")
print(f"Willow Fireworks: {fireworks['willow']}")
print(f"Crossette Fireworks: {fireworks['crossette']}")
