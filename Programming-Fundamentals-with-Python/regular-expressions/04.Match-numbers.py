import re

numbers_sequence = input()
pattern = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'

valid_numbers = [m_object.group() for m_object in re.finditer(pattern, numbers_sequence)]

print(*valid_numbers)
