users_number = int(input())
unique_users = set(input() for _ in range(users_number))
[print(user) for user in unique_users]
