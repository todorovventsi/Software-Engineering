import re


destinations = input()
pattern = r"(?P<del>[=/]{1})(?P<destination>[A-Z][a-zA-Z]{2,})(?P=del)"
valid_destinations = [item.group("destination") for item in re.finditer(pattern, destinations)]

print(f"Destinations: {', '.join(valid_destinations)}")
print(f"Travel Points: {sum([len(item) for item in valid_destinations])}")
