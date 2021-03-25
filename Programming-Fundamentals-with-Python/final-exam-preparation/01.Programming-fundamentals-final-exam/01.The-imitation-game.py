def move(num_letters, text):
    text = text[num_letters:] + text[:num_letters]
    return text


def insert(text, idx, val):
    if not idx < 0 or idx > len(text):
        text = text[:idx] + val + text[idx:]
    return text


def change(text, key_val, new_val):
    if key_val in text:
        text = text.replace(key_val, new_val)
    return text


message = input()
command = input()

while not command == "Decode":

    current_command = command.split("|")

    if current_command[0] == "Move":
        number_of_letters = int(current_command[1])
        message = move(number_of_letters, message)
    elif current_command[0] == "Insert":
        index = int(current_command[1])
        value = current_command[2]
        message = insert(message, index, value)
    elif current_command[0] == "ChangeAll":
        key_value = current_command[1]
        new_value = current_command[2]
        message = change(message, key_value, new_value)

    command = input()

print(f"The decrypted message is: {message}")
