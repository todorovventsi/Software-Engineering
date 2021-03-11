# triple quotes - functions documentation
# slicing
# substring

data = input()
ls = []
mats = {}
counter = 1
while not data == 'stop':
    ls.append(data)
    data = input()

for el in ls:
    if not counter % 2 == 0:
        if el not in mats:
            mats[el] = 0
    else:
        mats[ls[ls.index(el) - 1]] += int(el)
    counter += 1

for key, value in mats.items():
    print(f'{key} -> {value}')
