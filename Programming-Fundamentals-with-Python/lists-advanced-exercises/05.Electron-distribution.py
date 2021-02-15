electrons = int(input())

distribution_by_shell = []

for index in range(electrons):
    shell = index + 1
    max_electrons = 2 * shell ** 2
    if electrons > max_electrons:
        distribution_by_shell.append(max_electrons)
        electrons -= max_electrons
    elif electrons == max_electrons:
        distribution_by_shell.append(max_electrons)
        electrons -= max_electrons
        break
    else:
        distribution_by_shell.append(electrons)
        break

print(distribution_by_shell)