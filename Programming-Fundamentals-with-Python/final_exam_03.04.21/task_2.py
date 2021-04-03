import re

number_of_lines = int(input())
pattern = r'^(?P<symbols>.+)>(?P<g1>\d{3})\|(?P<g2>[a-z]{3})\|(?P<g3>[A-Z]{3})\|(?P<g4>[^<>]{3})<(?P=symbols)$'
for _ in range(number_of_lines):
    cyphered = input()
    match = re.match(pattern, cyphered)
    if match:
        result = match.group('g1') + match.group('g2') + match.group('g3') + match.group('g4')
        print(f"Password: {result}")
        continue
    print("Try another password!")
