import re

text = input()

p_emojis = r"(?P<sep>\*\*|::)(?P<emo>[A-Z][a-z][a-z]+)(?P=sep)"
p_digits = r"\d"

digits = re.findall(p_digits, text)
raw_emos = [item.group() for item in re.finditer(p_emojis, text)]
emojis = [item.group("emo") for item in re.finditer(p_emojis, text)]

cool_threshold = 1
for digit in digits:
    cool_threshold *= int(digit)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for emo in emojis:
    emo_coolness = 0
    for char in emo:
        emo_coolness += ord(char)
    if emo_coolness > cool_threshold:
        for e in raw_emos:
            if emo in e:
                print(e)
