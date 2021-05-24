numbers = input().split()
stack_of_numbers = []
while numbers:
    stack_of_numbers.append(numbers.pop())
print(*stack_of_numbers, sep=" ")
