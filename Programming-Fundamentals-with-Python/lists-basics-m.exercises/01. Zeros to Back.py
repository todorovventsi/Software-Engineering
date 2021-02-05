number_list = input().split(", ")

for index, value in enumerate(number_list):
    if value == "0":
        number_list.pop(index)
        number_list.extend(value)
new_numbers = [int(i) for i in number_list]

print(new_numbers)
