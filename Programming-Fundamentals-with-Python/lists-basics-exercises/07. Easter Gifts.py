planned_gifts = input()
gifts_listed = planned_gifts.split()

command = input()

while not command == "No Money":
    command_listed = command.split()
    # Checking "OutOfStock" command - Working
    if "OutOfStock" in command:
        missing_gift = command_listed[-1]
        for index in range(len(gifts_listed)):
            if gifts_listed[index] == missing_gift:
                gifts_listed[index] = "None"
    # Checking "Required" command - Working
    elif "Required" in command:
        index_to_replace = int(command_listed[2])
        if 0 <= index_to_replace < len(gifts_listed):
            gifts_listed[index_to_replace] = command_listed[1]
    # Checking "Just in case" command
    elif "JustInCase" in command:
        gifts_listed[-1] = command_listed[1]

    command = input()

# Excluding "Nones":
for gift in gifts_listed:
    if gift == "None":
        gifts_listed.remove(gift)

final_gifts = " ".join(gifts_listed)
print(final_gifts)
