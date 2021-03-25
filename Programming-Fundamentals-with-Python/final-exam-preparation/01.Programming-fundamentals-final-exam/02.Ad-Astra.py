import re

extraction_text = input()
food_pattern = r"(?P<del>[\|#])(?P<food_name>[a-zA-Z\s]+)(?P=del)(?P<expiration_date>\d{2}/\d{2}/\d{2})(?P=del)(?P<nutrition>\d{1,4}|10000)(?P=del)"

valid_foods = [match.groupdict() for match in re.finditer(food_pattern, extraction_text)]
total_calories = sum([int(match['nutrition']) for match in valid_foods])
days_covered = total_calories // 2000

print(f"You have food to last you for: {days_covered} days!")
for food in valid_foods:
    food_name = food["food_name"]
    expiration_date = food["expiration_date"]
    nutrition = food["nutrition"]
    print(f"Item: {food_name}, Best before: {expiration_date}, Nutrition: {nutrition}")
