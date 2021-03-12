to_extract = input()
text = input()

while to_extract in text:
    text = text.replace(to_extract, "")

print(text)
