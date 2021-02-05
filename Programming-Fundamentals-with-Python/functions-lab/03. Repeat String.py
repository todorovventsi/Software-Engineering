def repeat_string(string, n):
    result = ""
    for _ in range(n):
        result += string
    return result


text = input()
repeat_number = int(input())
output = repeat_string(text, repeat_number)
print(output)
