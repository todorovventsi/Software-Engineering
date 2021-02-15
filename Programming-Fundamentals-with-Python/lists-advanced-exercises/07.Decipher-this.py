ciphered_massage = input().split()

deciphered_massage = []
for word in ciphered_massage:
    num_as_list = list(filter(lambda x: x.isdigit(), word))
    word_as_list = list(filter(lambda x: not x.isdigit(), word))
    first_letter = chr(int("".join(num_as_list)))

    #Switching second and third letter
    word_as_list[0], word_as_list[-1] = word_as_list[-1], word_as_list[0]

    #Adding first letters
    word_as_list.insert(0, first_letter)
    deciphered_massage.append("".join(word_as_list))

print(*deciphered_massage)
