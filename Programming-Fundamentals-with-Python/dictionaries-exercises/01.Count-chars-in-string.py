string = input()

chars_counter = {}

for char in string:
    if char == " ":
        continue
    if char not in chars_counter:
        chars_counter[char] = 0
    chars_counter[char] += 1

for key, val in chars_counter.items():
    print(f"{key} -> {val}")
