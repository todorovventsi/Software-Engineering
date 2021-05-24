expression = input()
brackets_stack = []

for index in range(len(expression)):
    if expression[index] == "(":
        brackets_stack.append(index)
    elif expression[index] == ")":
        print(expression[brackets_stack.pop(): index + 1])
