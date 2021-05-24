number_of_queries = int(input())
stack_state = []

for _ in range(number_of_queries):
    command = input().split()
    if command[0] == "1":
        stack_state.append(int(command[1]))
    elif command[0] == "2":
        if stack_state:
            stack_state.pop()
    elif command[0] == "3":
        if stack_state:
            print(max(stack_state))
    elif command[0] == "4":
        if stack_state:
            print(min(stack_state))
if stack_state:
    stack_print = [stack_state.pop() for _ in range(len(stack_state))]
    print(*stack_print, sep=", ")
