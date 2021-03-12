data = input().split()

output = 0
diff = 0
if not len(data[0]) == len(data[1]):
    diff = abs(len(data[0]) - len(data[1]))
    data.sort(key=lambda x: -len(x))  # Longest always on first place

multiply_times = len(data[0]) - diff

for index in range(multiply_times):
    result = ord(data[0][index]) * ord(data[1][index])
    output += result

remaining = data[0][len(data[1])::]
for index in range(diff):
    output += ord(remaining[index])

print(output)
