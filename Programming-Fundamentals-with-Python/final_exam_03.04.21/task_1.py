initial_string = input()

command = input()

while not command == "End":
    data = command.split()
    if "Translate" in data:
        ch = data[1]
        rep = data[2]
        initial_string = initial_string.replace(ch, rep)
        print(initial_string)
    elif "Includes" in data:
        to_check = data[1]
        if to_check in initial_string:
            print("True")
        else:
            print("False")
    elif "Start" in data:
        to_check = data[1]
        print(initial_string.startswith(to_check))
    elif "Lowercase" in data:
        initial_string = initial_string.lower()
        print(initial_string)
    elif "FindIndex" in data:
        print(initial_string.rfind(data[1]))
    elif "Remove" in data:
        str_in = int(data[1])
        count = int(data[2])
        to_remove = initial_string[str_in:str_in + count]
        initial_string = initial_string.replace(to_remove, "")
        print(initial_string)


    command = input()
