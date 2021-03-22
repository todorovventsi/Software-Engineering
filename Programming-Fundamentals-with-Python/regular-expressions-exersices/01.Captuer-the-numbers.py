import re

text_line = input()
numbers = []

while text_line:
    line_nums = re.findall(r"\d+", text_line)
    numbers.extend(line_nums)

    text_line = input()

print(*numbers)
