neighborhood = [int(i) for i in input().split("@")]

command = input()
last_visited = 0
while "Love!" not in command:
    jump, length = command.split()
    if last_visited + int(length) > len(neighborhood) - 1:
        last_visited = 0
    else:
        last_visited += int(length)
    neighborhood[last_visited] -= 2
    if neighborhood[last_visited] == 0:
        print(f"Place {last_visited} has Valentine's day.")
    elif neighborhood[last_visited] < 0:
        print(f"Place {last_visited} already had Valentine's day.")
    command = input()

print(f"Cupid's last position was {last_visited}.")
if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {sum(not i <= 0 for i in neighborhood)} places.")
