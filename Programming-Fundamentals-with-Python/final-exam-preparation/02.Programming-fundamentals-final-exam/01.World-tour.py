def index_is_valid(i, strn):
    if 0 <= i < len(strn):
        return True
    return False


def add_stop(i, to_add, origin):
    result = origin[:i] + to_add + origin[i:]
    return result


def remove_stop(s_inx, e_inx, origin):
    result = origin[:s_inx] + origin[e_inx+1:]
    return result


def switch_destination(old, new, origin):
    result = origin.replace(old, new)
    return result


destinations = input()

command = input()
while not command == "Travel":
    data = command.split(":")
    if "Add Stop" in data:
        index = int(data[1])
        destination = data[2]
        if index_is_valid(index, destinations):
            destinations = add_stop(index, destination, destinations)
        print(destinations)
    elif "Remove Stop" in data:
        s_index = int(data[1])
        e_index = int(data[2])
        if index_is_valid(s_index, destinations) and index_is_valid(e_index, destinations):
            destinations = remove_stop(s_index, e_index, destinations)
        print(destinations)
    elif "Switch" in data:
        old_string = data[1]
        new_string = data[2]
        if old_string in destinations:
            destinations = switch_destination(old_string, new_string, destinations)
        print(destinations)

    command = input()

print(f"Ready for world tour! Planned stops: {destinations}")
