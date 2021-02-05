number = int(input())

isPrime = True

for num in range(2, number):
    if number % num == 0:
        isPrime = False
        break
print(isPrime)
