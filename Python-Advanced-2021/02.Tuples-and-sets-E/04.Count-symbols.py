characters_sequence = input()

char_dict = {}

for char in characters_sequence:
    if char not in char_dict:
        char_dict[char] = characters_sequence.count(char)

alphbet_sorted = sorted(char_dict.items())
[print(f"{symbol}: {count} time/s") for symbol, count in alphbet_sorted]
