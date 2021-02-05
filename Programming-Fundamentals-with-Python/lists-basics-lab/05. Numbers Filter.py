number_of_inputs = int(input())

evens = []
odds = []
positive = []
negative = []

for _ in range(number_of_inputs):
    number = int(input())

    if number % 2 == 0:
        evens.append(number)
    else:
        odds.append(number)
    if number < 0:
        negative.append(number)
    else:
        positive.append(number)

command = input()
if command == "even":
    print(evens)
elif command == "odd":
    print(odds)
elif command == "positive":
    print(positive)
else:
    print(negative)
