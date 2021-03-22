def string_slice(string, start, end):
    first_half = string[:start]
    second_half = string[end:]
    result = first_half + second_half
    return result


def switch_cases(string, case, start, end):
    sequence = string[start:end]
    if case == "Upper":
        string = string.replace(sequence, sequence.upper())
    else:
        string = string.replace(sequence, sequence.lower())
    return string


raw_key = input()

command = input()
while not command == "Generate":
    data = command.split(">>>")
    if "Contains" in command:
        substring = data[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")
    elif "Flip" in command:
        cases = data[1]
        starting_i = int(data[2])
        ending_i = int(data[3])
        raw_key = switch_cases(raw_key, cases, starting_i, ending_i)
        print(raw_key)
    elif "Slice" in command:
        starting_i = int(data[1])
        ending_i = int(data[2])
        raw_key = string_slice(raw_key, starting_i, ending_i)
        print(raw_key)

    command = input()

print(f"Your activation key is: {raw_key}")
