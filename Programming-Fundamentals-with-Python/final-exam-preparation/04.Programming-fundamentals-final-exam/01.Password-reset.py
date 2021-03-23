def remove_evens(string):
    temp = ""
    for index in range(0, len(string)):
        if not index % 2 == 0:
            temp += string[index]
    return temp


def remove_substring(string, start, end):
    substring = string[start:end]
    string = string.replace(substring, "", 1)
    return string


def substitute_str(string, old, new):
    string = string.replace(old, new)
    return string


password = input()
command = input()

while not command == "Done":
    data = command.split()
    if "TakeOdd" in data:
        password = remove_evens(password)
        print(password)
    elif "Cut" in data:
        start_i = int(data[1])
        end_i = start_i + int(data[2])
        password = remove_substring(password, start_i, end_i)
        print(password)
    elif "Substitute" in data:
        substring = data[1]
        substitute = data[2]
        if substring not in password:
            print("Nothing to replace!")
            command = input()
            continue
        password = substitute_str(password, substring, substitute)
        print(password)

    command = input()

print(f"Your password is: {password}")
