numbers = input()
number_of_beggars = int(input())

listed_numbers = numbers.split(", ")
result = []

for beggar in range(number_of_beggars):
    beggar_collected = 0
    for index in range(beggar, len(listed_numbers), number_of_beggars):
        beggar_collected += int(listed_numbers[index])
    result.append(beggar_collected)

print(result)
