def d_type_manipulator(comm, t_object):
    result = ""
    if comm == "int":
        result = int(t_object) * 2
    elif comm == "real":
        result = f"{float(t_object) * 1.5:.2f}"
    elif comm == "string":
        result = f"${t_object}$"
    return result


command = input()
target_object = input()
print(d_type_manipulator(command, target_object))
