def print_chars_in_between(char1, char2):
    result = ""
    if ord(char1) > ord(char2):
        for char in range(ord(char2) + 1, ord(char1)):
            result += chr(char) + " "
    else:
        for char in range(ord(char1) + 1, ord(char2)):
            result += chr(char) + " "
    return result


first_char = input()
second_char = input()
sequence = print_chars_in_between(first_char, second_char)
print(sequence)
