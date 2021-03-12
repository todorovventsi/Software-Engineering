sequence = input()

index = 0

while index < len(sequence):
    strength = 0
    symbol = sequence[index]
    right_to_symbol = sequence[index + 1]
    if symbol == ">" and right_to_symbol.isdigit():
        strength += int(right_to_symbol)
        for char in range(index + 1, index + int(right_to_symbol) + 1):
            pass

    index += 1

print(sequence)



