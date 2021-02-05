def check_length(password):
    # returns True if password length is valid and False if it is not
    if 6 <= len(password) <= 10:
        return True
    return False


def check_forbidden_symbols(password):
    # The password must contain only letters and digits.
    # Returns True if the password is valid and false if it is not
    is_valid = True
    for char in password:
        if not (48 <= ord(char) <= 57 or 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122):
            is_valid = False
            break
    if is_valid:
        return True
    return False


def digits_number_check(password):
    # Returns True if digits are at least 2, otherwise returns False
    digits = 0
    for char in password:
        if 48 <= ord(char) <= 57:
            digits += 1
    if digits < 2:
        return False
    return True


def final_check(password):
    password_is_valid = True
    if not check_length(password):
        print("Password must be between 6 and 10 characters")
        password_is_valid = False
    if not check_forbidden_symbols(password):
        print("Password must consist only of letters and digits")
        password_is_valid = False
    if not digits_number_check(password):
        print("Password must have at least 2 digits")
        password_is_valid = False
    if password_is_valid:
        print("Password is valid")


password_to_be_validated = input()
final_check(password_to_be_validated)
