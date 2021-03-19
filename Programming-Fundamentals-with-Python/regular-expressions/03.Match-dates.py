import re

dates_sequence = input()
pattern = r"\b(?P<Day>\d{2})(?P<Sep>[\.\-\/])(?P<Month>[A-Z][a-z]{2})(?P=Sep)(?P<Year>\d{4})\b"
valid_dates = re.finditer(pattern, dates_sequence)
for date in valid_dates:
    print(f"Day: {date['Day']}, Month: {date['Month']}, Year: {date['Year']}")
