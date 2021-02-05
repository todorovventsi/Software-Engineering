def polindrome_check(list_of_numbers_as_strings):
    for number in list_of_numbers_as_strings:
        left_to_right = int(number)
        current_to_list = list(number)
        current_to_list.reverse()
        right_to_left = int("".join(current_to_list))
        if left_to_right == right_to_left:
            print(True)
        else:
            print(False)


numbers_to_check = input().split(", ")
polindrome_check(numbers_to_check)
