import re

text = input()

pattern = r'www\.[a-zA-Z0-9\-]+(\.[a-z]+)+'
valid_addresses = []

while text:
    valids = [item.group() for item in re.finditer(pattern, text)]
    valid_addresses.extend(valids)

    text = input()

print(*valid_addresses, sep="\n")
