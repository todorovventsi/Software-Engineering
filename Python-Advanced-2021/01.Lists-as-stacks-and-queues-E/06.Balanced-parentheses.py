from collections import deque


expression = list(input())
parentheses_stack = deque()

expr_is_balanced = True

for symbol in expression:
    if symbol == "(" or symbol == "{" or symbol == "[":
        parentheses_stack.append(symbol)
    elif symbol == ")":
        if parentheses_stack:
            if parentheses_stack[-1] == "(":
                parentheses_stack.pop()
                continue
            else:
                expr_is_balanced = False
                break
    elif symbol == "}":
        if parentheses_stack:
            if parentheses_stack[-1] == "{":
                parentheses_stack.pop()
                continue
            else:
                expr_is_balanced = False
                break
    elif symbol == "]":
        if parentheses_stack:
            if parentheses_stack[-1] == "[":
                parentheses_stack.pop()
                continue
            else:
                expr_is_balanced = False
                break
    else:
        expr_is_balanced = False
        break

if expr_is_balanced:
    print("YES")
else:
    print("NO")
