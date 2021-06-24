from collections import deque


#Inputs:
bomb_effects = deque([int(i) for i in input().split(', ')])
bomb_casings = deque([int(i) for i in input().split(', ')])

materials = {40: "Datura Bombs",60: "Cherry Bombs",120: "Smoke Decoy Bombs"}
bombs_record = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}
pouch_is_filled = True

while bomb_effects and bomb_casings:
    bomb_value = bomb_effects[0] + bomb_casings[-1]
    if bomb_value in materials:
        current_bomb = materials[bomb_value]
        bombs_record[current_bomb] += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5
    for bomb, value in bombs_record.items():
        if value >= 3:
            pouch_is_filled = True
            continue
        pouch_is_filled = False
        break
    if pouch_is_filled:
        break

print("Bene! You have successfully filled the bomb pouch!" if pouch_is_filled else "You don't have enough materials to fill the bomb pouch.")
print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}" if bomb_effects else "Bomb Effects: empty")
print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}" if bomb_casings else "Bomb Casings: empty")
[print(f"{bomb}: {value}") for bomb, value in sorted(bombs_record.items())]
