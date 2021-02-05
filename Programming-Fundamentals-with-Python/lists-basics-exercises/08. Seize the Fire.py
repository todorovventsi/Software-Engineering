fire_input = input()
water_in_hands = int(input())

effort = 0
total_fire = 0
fire_cells = fire_input.split("#")

print("Cells:")
for fire in range(len(fire_cells)):
    current_fire = fire_cells[fire].split(" = ")
    # fire validation
    if "High" in current_fire and (not 81 <= int(current_fire[-1]) <= 125):
        continue
    elif "Medium" in current_fire and (not 51 <= int(current_fire[-1]) <= 80):
        continue
    elif "Low" in current_fire and (not 1 <= int(current_fire[-1]) <= 50):
        continue

    # water quantity validation:
    if water_in_hands < int(current_fire[-1]):
        continue

    effort += 0.25 * int(current_fire[-1])
    total_fire += int(current_fire[-1])
    water_in_hands -= int(current_fire[-1])
    print(f" - {current_fire[-1]}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
