data = input().split()

for word in data:
    print(f"{word * len(word)}", end="")
