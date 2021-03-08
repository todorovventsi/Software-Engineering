company_register = {}

data = input()

while not data == "End":
    company, user_id = data.split(" -> ")
    if company not in company_register:
        company_register[company] = []
    if user_id in company_register[company]:
        data = input()
        continue
    company_register[company].append(user_id)

    data = input()

company_register_sorted = dict(sorted(company_register.items()))
for company, ids in company_register_sorted.items():
    print(f"{company}")
    for current_id in ids:
        print(f"-- {current_id}")
