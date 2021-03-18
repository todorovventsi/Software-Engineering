import re
numbers = input()

pattern = r"\+359( |-)2\1\d{3}\1\d{4}\b"

valid_numbers = [item.group() for item in re.finditer(pattern, numbers)]
print(*valid_numbers, sep=", ")
