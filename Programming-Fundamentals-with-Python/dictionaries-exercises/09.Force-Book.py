import re


def user_exist(dict_to_check, force, user):
    if user in dict_to_check[force]:
        return True
    return False


def force_exist(c_dict, force):
    if force in c_dict:
        return True
    return False


force_book = {}

command = input()

while not command == "Lumpawaroo":
    data = re.split("->|\\|", "".join(command))
    force_side, force_user = data[0], data[1]
    if "|" in command:
        pass
    else:
        pass
    command = input()
