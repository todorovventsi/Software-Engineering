def user_exist(c_dict, value):
    # Checks if a given user exist in the forcebook
    # Accepts dictionary (forcebook), key(force) and value(user)
    for val in c_dict.values():
        if value in val:
            return True
    return False


def force_exist(c_dict, force):
    # Checks if a given force exist in force_book
    # Accepts dictionary (forcebook), and a key(force)
    if force in c_dict:
        return True
    return False


def add_user(c_dict, key, value):
    # Add a user to a given force in the forcebook
    # Accepts dictionary (forcebook), key(force) and a value(user)
    c_dict[key].append(value)


force_book = {}

command = input()

while not command == "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(" | ")
        if not force_exist(force_book, force_side):
            force_book[force_side] = []
        if not user_exist(force_book, force_user):
            add_user(force_book, force_side, force_user)
    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        if user_exist(force_book, force_user):
            old_side = [side for side in force_book if not side == force_side][0]
            force_book[old_side].remove(force_user)
            force_book[force_side].append(force_user)
        else:
            add_user(force_book, force_side, force_user)
        print(f"{force_user} joins the {force_side} side!")

    command = input()


sorted_book = dict(sorted(force_book.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))

for side, users in sorted_book.items():
    if users:
        print(f"Side: {side}, Members: {len(users)}")
        users.sort()
        for user in users:
            print(f"! {user}")
