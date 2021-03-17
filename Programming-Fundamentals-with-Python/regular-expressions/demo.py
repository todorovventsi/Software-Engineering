import re

s = "foo123bar"
pattern = re.compile(r'\d{3}')

result = re.search(pattern, s)
print(result)
