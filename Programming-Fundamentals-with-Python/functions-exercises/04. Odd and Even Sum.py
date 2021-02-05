def odd_even_count(given_number_as_string):
    odd_even_list = [0, 0]
    for digit in given_number_as_string:
        if int(digit) % 2 == 0:
            odd_even_list[1] += int(digit)
        else:
            odd_even_list[0] += int(digit)
    return odd_even_list


initial_number_as_string = input()
list_of_numbers = odd_even_count(initial_number_as_string)
evens = list_of_numbers[1]
odds = list_of_numbers[0]

print(f"Odd sum = {odds}, Even sum = {evens}")
