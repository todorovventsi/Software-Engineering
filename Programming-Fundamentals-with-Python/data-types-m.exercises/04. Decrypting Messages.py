key = int(input())
lines = int(input())
massage = ""

for char in range(lines):
    character = input()
    decrypted = chr(ord(character) + key)
    massage += decrypted
print(massage)
