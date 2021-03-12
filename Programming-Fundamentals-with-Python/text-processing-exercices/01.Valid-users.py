def contain_valid_symbols(name):
    symbols = list(name)
    for ch in symbols:
        if not ch.isalnum():
            if ch == "-" or ch == "_":
                break
            return False
    return True


user_names = input().split(", ")
valid_user_names = []

for user_name in user_names:
    if 3 < len(user_name) < 16:
        if contain_valid_symbols(user_name):
            valid_user_names.append(user_name)

for user in valid_user_names:
    print(user)
