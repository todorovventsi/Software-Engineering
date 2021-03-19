import re

text = input()
pattern = r'(^_|(?<=\s_)){1}[a-zA-Z0-9]+\b'

valid_variables = [variable.group() for variable in re.finditer(pattern, text)]
print(*valid_variables, sep=",")
