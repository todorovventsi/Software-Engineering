string_of_numbers = input()

list_of_symbols = string_of_numbers.split(sep=" ")
inverted_list = []

for symbol in list_of_symbols:
    inverted_symbol = int(symbol) * (-1)
    inverted_list.append(inverted_symbol)
print(inverted_list)
