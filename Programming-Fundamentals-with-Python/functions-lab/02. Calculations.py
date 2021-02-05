def calculate(action, num1, num2):
    if action == "multiply":
        return num1 * num2
    elif action == "divide":
        return  num1 // num2
    elif action == "add":
        return num1 + num2
    elif action == "subtract":
        return num1 - num2


action = input()
number_one = int(input())
number_two = int(input())
result = calculate(action, number_one, number_two)
print(result)
