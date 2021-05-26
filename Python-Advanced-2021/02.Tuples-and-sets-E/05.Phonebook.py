phone_register = {}

while True:
    info = input()
    if info.isdigit():
        break
    name, number = info.split("-")
    if name not in phone_register:
        phone_register[name] = 0
    phone_register[name] = number

for _ in range(int(info)):
    contact = input()
    if contact in phone_register:
        print(f"{contact} -> {phone_register[contact]}")
        continue
    print(f"Contact {contact} does not exist.")
