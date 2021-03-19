import re

numbers_sequence = input()
pattern = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'

valid_numbers = re.finditer(pattern, numbers_sequence)

for number in valid_numbers:
    print(number.group(), end=" ")
