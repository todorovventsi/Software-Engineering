n = int(input())

register = {}

for _ in range(n):
    data = input().split()
    command = data[0]
    username = data[1]
    if command == "register":
        licence = data[2]
        if username in register:
            print(f"ERROR: already registered with plate number {licence}")
            continue
        else:
            register[username] = licence
            print(f"{username} registered {licence} successfully")
    else:
        if username not in register:
            print(f"ERROR: user {username} not found")
            continue
        else:
            register.pop(username)
            print(f"{username} unregistered successfully")

for user, licence in register.items():
    print(f"{user} => {licence}")
