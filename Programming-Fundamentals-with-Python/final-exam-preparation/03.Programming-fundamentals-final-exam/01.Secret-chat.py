secret_massage = input()
command = input()

while not command == "Reveal":
    data = command.split(":|:")
    if "InsertSpace" in data:
        index = int(data[1])
        first = secret_massage[:index]
        second = secret_massage[index:]
        secret_massage = first + " " + second
        print(secret_massage)
    elif "Reverse" in data:
        substring = data[1]
        if substring not in secret_massage:
            print("error")
            command = input()
            continue
        secret_massage = secret_massage.replace(substring, "", 1)
        secret_massage += substring[::-1]
        print(secret_massage)
    elif "ChangeAll" in data:
        substring = data[1]
        replacement = data[2]
        secret_massage = secret_massage.replace(substring, replacement)
        print(secret_massage)

    command = input()

print(f"You have a new text message: {secret_massage}")
