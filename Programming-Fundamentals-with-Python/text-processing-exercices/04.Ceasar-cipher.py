to_encode = input()
encrypted = ""
for ch in to_encode:
    encrypted += chr(ord(ch) + 3)

print(encrypted)
