text = input()

print(''.join([x for x in text if x.isdigit()]))
print(''.join([x for x in text if x.isalpha()]))
print(''.join([x for x in text if not x.isalnum()]))