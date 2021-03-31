all_contests = {}
unique_users = []
users_total_score = {}

data = input()
while not data == "no more time":
    username, contest, points = data.split(" -> ")
    points = int(points)
    if contest not in all_contests:
        all_contests[contest] = {}
    if username not in all_contests[contest]:
        all_contests[contest][username] = points
    if all_contests[contest][username] < points:
        all_contests[contest][username] = points

    data = input()

for contest, users in all_contests.items():
    for user in users:
        if user not in unique_users:
            unique_users.append(user)

for user in unique_users:
    if user not in users_total_score:
        users_total_score[user] = 0
    for content, users in all_contests.items():
        if user in users:
            users_total_score[user] += all_contests[content][user]

for contest, participants in all_contests.items():
    print(f"{contest}: {len(participants)} participants")
    position = 1
    for user, points in sorted(participants.items(), key=lambda kvp: (-kvp[1], kvp[0])):
        print(f"{position}. {user} <::> {points}")
        position += 1

print("Individual standings:")
position = 1
for user, points in sorted(users_total_score.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f"{position}. {user} -> {points}")
    position += 1
