string = input()

index = 0

while index < len(string) - 1:
    if string[index] == string[index + 1]:
        to_replace = f"{string[index]}{string[index + 1]}"
        string = string.replace(to_replace, string[index])
        index = 0
    else:
        index += 1

print(string)
