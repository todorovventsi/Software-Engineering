def exchange(array, ind):
    arr_one = array[:ind + 1]
    arr_two = array[ind + 1::]
    result = arr_two + arr_one
    return result


def min_or_max(array, arr_evens, arr_odds, min_max, even_odd):
    result = 0
    if min_max == "max":
        if even_odd == "even":  # Max even
            if not arr_evens:
                result = "No matches"
                return result
            max_even = max(arr_evens)
            if array.count(max_even) == 1:
                result = array.index(max_even)
                return result
            else:
                result = len(array) - array[::-1].index(max_even) - 1
        elif even_odd == "odd":  # Max odd
            if not arr_odds:
                result = "No matches"
                return result
            max_odd = max(arr_odds)
            if array.count(max_odd) == 1:
                result = array.index(max_odd)
                return result
            else:
                result = len(array) - array[::-1].index(max_odd) - 1

    elif min_max == "min":
        if even_odd == "even":  # Max even
            if not arr_evens:
                result = "No matches"
                return result
            max_even = min(arr_evens)
            if array.count(max_even) == 1:
                result = array.index(max_even)
                return result
            else:
                result = len(array) - array[::-1].index(max_even) - 1
        elif even_odd == "odd":  # Max odd
            if not arr_odds:
                result = "No matches"
                return result
            max_odd = min(arr_odds)
            if array.count(max_odd) == 1:
                result = array.index(max_odd)
                return result
            else:
                result = len(array) - array[::-1].index(max_odd) - 1


def first_or_last(array, first_last, val, even_odd):
    evens = [x for x in array if x % 2 == 0]
    odds = [x for x in array if not x % 2 == 0]
    result = 0
    if val > len(array):
        result = "Invalid count"
        return result

    if first_last == "first":
        if even_odd == "even":
            if not evens:
                result = []
                return result
            if val > len(evens):
                result = evens
                return result
            result = evens[:val]
            return result
        elif even_odd == "odd":
            if not odds:
                result = []
                return result
            if val > len(odds):
                result = odds
                return result
            result = odds[:val]
            return result

    elif first_last == "last":
        if even_odd == "even":
            if not evens:
                result = []
                return result
            if val > len(evens):
                result = evens
                return result
            result = evens[len(evens):val:-1]
            return result
        elif even_odd == "odd":
            if not odds:
                result = []
                return result
            if val > len(odds):
                result = odds
                return result
            result = odds[len(odds):val:-1]
            return result


initial_array = [int(i) for i in input().split()]
evens = [x for x in initial_array if x % 2 == 0]
odds = [x for x in initial_array if not x % 2 == 0]

command = input()

while not command == "end":
    command = command.split()

    if "exchange" in command:
        index = int(command[1])
        if index in range(len(initial_array)):
            initial_array = exchange(initial_array, index)
        else:
            print("Invalid index")

    elif "max" in command or "min" in command:
        criteria = command[0]
        even_or_odd = command[1]
        output = min_or_max(initial_array, evens, odds, criteria, even_or_odd)
        print(output)


    elif "first" in command or "last" in command:
        criteria = command[0]
        value = int(command[1])
        even_or_odd = command[2]
        output = first_or_last(initial_array, criteria, value, even_or_odd)
        print(output)

    command = input()

print(initial_array)
