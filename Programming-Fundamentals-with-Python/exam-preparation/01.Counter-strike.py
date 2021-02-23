energy = int(input())
won_battles = 0
game_ended = False
command = input()

while not command == "End of battle":
    distance = int(command)
    if distance <= energy:
        energy -= distance
        won_battles += 1
    else:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
        game_ended = True
        break
    if won_battles % 3 == 0:
        energy += won_battles
    command = input()

if not game_ended:
    print(f"Won battles: {won_battles}. Energy left: {energy}")
