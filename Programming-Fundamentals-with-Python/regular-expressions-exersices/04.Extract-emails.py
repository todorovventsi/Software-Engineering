import re

emails = input()
pattern = r'(^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-z]+-?[a-z]+(\.[a-z]+)+'
valid_emails = [matched_obj.group() for matched_obj in re.finditer(pattern, emails)]
print(*valid_emails, sep="\n")
