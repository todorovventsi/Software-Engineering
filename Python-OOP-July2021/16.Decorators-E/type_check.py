def type_check(type_to_check):
    def decorator(func):
        def wrapper(arg):
            if type_to_check == type(arg):
                result = func(arg)
                return result
            return "Bad Type"
        return wrapper
    return decorator


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
