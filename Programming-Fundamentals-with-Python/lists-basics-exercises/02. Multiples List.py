factor = int(input())
count = int(input())

resulted_list = []
number = 1
while len(resulted_list) < count:
    if number % factor == 0:
        resulted_list.append(number)
    number += 1

print(resulted_list)
