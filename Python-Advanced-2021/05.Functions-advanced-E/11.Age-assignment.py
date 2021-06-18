def age_assignment(*args, **kwargs):
    result = {}
    for name in args:
        result[name] = kwargs.get(name[0])
    return result


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
