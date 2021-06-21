def flights(*args):
    record = {}
    for i in range(0, len(args)):
        arg = args[i]
        if arg == "Finish":
            break
        if isinstance(arg, str):
            if arg not in record:
                record[arg] = 0
            record[arg] += args[i + 1]
    return record

print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
