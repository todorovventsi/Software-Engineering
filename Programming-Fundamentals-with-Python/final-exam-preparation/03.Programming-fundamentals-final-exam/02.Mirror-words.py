import re

text = input()

pattern = r"(?P<del>[@#])(?P<wordone>[a-zA-Z]{3,})(?P=del){2}(?P<wordtwo>[a-zA-Z]{3,})(?P=del)"
matches = [match.groupdict() for match in re.finditer(pattern, text)]
if not matches:
    print("No word pairs found!")
    print("No mirror words!")
else:
    print(f"{len(matches)} word pairs found!")
    mirrors = {}
    for index in range(len(matches)):
        if matches[index]['wordone'] == matches[index]['wordtwo'][::-1]:
            mirrors[f"Pair {index + 1}"] = [matches[index]['wordone'], matches[index]['wordtwo']]
    if mirrors:
        print("The mirror words are:")
        output = []
        for pair, values in mirrors.items():
            output.append(f"{values[0]} <=> {values[1]}")
        print(*output, sep=", ")
    else:
        print("No mirror words!")
