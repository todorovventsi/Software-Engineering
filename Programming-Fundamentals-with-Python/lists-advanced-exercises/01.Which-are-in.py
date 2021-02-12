# first_s = input().split(", ")
# second_s = input()
#
# resulting_s = [word for word in first_s if word in second_s]
# # resulting_s = list(filter(lambda word: word in second_s, first_s))
# print(resulting_s)
first_list = input().split(", ")
second_list = input().split(", ")
second_list_strings = "".join(second_list)
new_list = [word for word in first_list if word in second_list_strings]
set(new_list)
print(new_list)