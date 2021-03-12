to_encode = input()
encrypted = []
for ch in to_encode:
    encrypted.append(chr(ord(ch) + 3))

print(''.join(encrypted))
