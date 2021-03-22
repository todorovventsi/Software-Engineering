import re

emails = input()
pattern = r'\b[a-zA-Z0-9]+[\.\-\_]?([a-zA-Z0-9]+)*@([a-zA-Z0-9]+\-?[a-zA-Z0-9]+)(\.[a-zA-Z0-9]+\-?[a-zA-Z0-9]+)+'
valid_emails = [matched_obj.group() for matched_obj in re.finditer(pattern, emails)]
print(*valid_emails, sep="\n")
