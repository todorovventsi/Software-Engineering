targets = list(map(int, input().split()))
# targets = [int(i) for i in input().split()]

command = input()

while not command == "End":
    shooting_index = int(command)
    if not 0 <= shooting_index < len(targets):
        command = input()
        continue
    index_value = targets[shooting_index]
    targets[shooting_index] = - 1
    for ind in range(0, len(targets)):
        if targets[ind] > index_value and not targets[ind] == -1:
            targets[ind] -= index_value
        elif targets[ind] <= index_value and not targets[ind] == -1:
            targets[ind] += index_value
    command = input()

print(f"Shot targets: {targets.count(-1)} -> ", end="")
print(*targets)