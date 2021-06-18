start_i = int(input())
end_i = int(input())

result = [num for num in range(start_i, end_i + 1) if [el for el in range(2, 11) if num % el == 0]]
print(result)
