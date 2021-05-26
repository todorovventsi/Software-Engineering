number_of_names = int(input())

names_register = set()
[names_register.add(input()) for _ in range(number_of_names)]
print(*names_register, sep="\n")
