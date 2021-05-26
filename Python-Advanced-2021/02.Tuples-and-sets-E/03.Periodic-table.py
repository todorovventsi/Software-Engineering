number_of_compounds = int(input())

unique_elements = set()
for _ in range(number_of_compounds):
    content = input().split()
    for element in content:
        unique_elements.add(element)
print(*unique_elements, sep="\n")
