# Define a function that splits a list into two different lists and exchange their places into a new list:
def exchange_list(working_list, index):
    if index >= len(working_list) or index < -len(working_list):
        return "Invalid index"

    temp1 = working_list[:index + 1]
    temp2 = working_list[index + 1:]
    result = temp2 + temp1
    return result


def min_max_even_odd(working_list, com):
    evens = []
    odds = []
    for num in working_list:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)

    if "even" in com and "min" in com:
        if not evens:
            result = "No matches"
            return result

        min_even = min(evens)
        min_evens = evens.count(min_even)

        if min_evens > 1:
            for index in range(len(working_list) - 1, -1, -1):
                if working_list[index] == min_even:
                    return index
        return working_list.index(min_even)

    elif "even" in com and "max" in com:
        if not evens:
            result = "No matches"
            return result

        max_even = max(evens)
        max_evens = evens.count(max_even)

        if max_evens > 1:
            for index in range(len(working_list) - 1, -1, -1):
                if working_list[index] == max_even:
                    return index
        return working_list.index(max_even)

    elif "odd" in com and "min" in com:
        if not odds:
            result = "No matches"
            return result

        min_odd = min(odds)
        min_odds = odds.count(min_odd)

        if min_odds > 1:
            for index in range(len(working_list) - 1, -1, -1):
                if working_list[index] == min_odd:
                    return index
        return working_list.index(min_odd)

    elif "odd" in com and "max" in com:
        if not odds:
            result = "No matches"
            return result

        max_odd = max(odds)
        max_odds = odds.count(max_odd)

        if max_odds > 1:
            for index in range(len(working_list) - 1, -1, -1):
                if working_list[index] == max_odd:
                    return index
        return working_list.index(max_odd)


def first_last_even_odd(working_list, com):
    result = []
    if int(com[1]) > len(working_list):
        return "Invalid count"
    if "first" in com and "even" in com:
        count = 0
        for num in working_list:
            if num % 2 == 0:
                result.append(num)
                count += 1
            if count == int(com[1]):
                break

    elif "first" in com and "odd" in com:
        count = 0
        for num in working_list:
            if not num % 2 == 0:
                result.append(num)
                count += 1
            if count == int(com[1]):
                break

    elif "last" in com and "even" in com:
        count = 0
        for index in range(len(working_list) - 1, -1, -1):
            if working_list[index] % 2 == 0:
                result.append(working_list[index])
                count += 1
            if count == int(com[1]):
                break

    elif "last" in com and "odd" in com:
        count = 0
        for index in range(len(working_list) - 1, -1, -1):
            if not working_list[index] % 2 == 0:
                result.append(working_list[index])
                count += 1
            if count == int(com[1]):
                break

    return result


input_list = [int(i) for i in input().split()]
command = input()

while not command == "end":
    command_as_list = command.split()
    if "exchange" in command:
        result = exchange_list(input_list, int(command_as_list[-1]))
        if result == "Invalid index":
            print(result)
        else:
            input_list = result

    if "max" in command or "min" in command:
        print(min_max_even_odd(input_list, command_as_list))

    if "first" in command or "last" in command:
        print(first_last_even_odd(input_list, command_as_list))

    command = input()

print(input_list)
