employees_happiness = list(map(int, input().split()))
improvement_factor = int(input())

improved_happiness = list(map(lambda x: x * improvement_factor, employees_happiness))
avg_happiness = sum(improved_happiness) / len(improved_happiness)
happy_employees = list(filter(lambda x: x >= avg_happiness, improved_happiness))

happy_count = len(happy_employees)
total_count = len(improved_happiness)

if happy_count >= total_count / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")
