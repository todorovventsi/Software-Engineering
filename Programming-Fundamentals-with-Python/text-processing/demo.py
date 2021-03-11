# triple quotes - functions documentation
# slicing
# substring

to_remove = input()
text = input()

while to_remove in text:
    text = text.replace(to_remove, "")

print(text)
