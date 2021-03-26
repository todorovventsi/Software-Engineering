def is_contest_valid(con, pass_w, register):
    if con in register and register[con] == pass_w:
        return True
    return False


contests_data = {}
contest_users = {}

contests = input()
while not contests == "end of contests":
    contest, password = contests.split(":")
    contests_data[contest] = password

    contests = input()

users_data = input()
while not users_data == "end of submissions":
    contest, password, user, points = users_data.split("=>")
    points = int(points)
    if is_contest_valid(contest, password, contests_data):
        if contest in contest_users and user in contest_users[contest]:
            if points > contest_users[contest][user]:
                contest_users[contest][user] = points
                continue
        update_data = {user: points}
        if contest not in contest_users:
            contest_users[contest] = {}
        if user not in contest_users[contest]:
            contest_users[contest].update(update_data)
        else:
            if contest_users[contest][user] < points:
                contest_users[contest].update(update_data)
    users_data = input()

users_total_scores = {}
for contest in contest_users.values():
    for user in contest:
        if user not in users_total_scores:
            users_total_scores[user] = 0
        users_total_scores[user] += contest[user]

ranking_sort = sorted(users_total_scores.items(), key=lambda value: -value[1])
name_sort = sorted(users_total_scores.items(), key=lambda value: value[0])
# contest_users = dict(sorted(contest_users.items(), key=lambda kvp: kvp[0]))

print(f"Best candidate is {ranking_sort[0][0]} with total {ranking_sort[0][1]} points.")
print("Ranking:")
for user in name_sort:
    name = user[0]
    print(name)
    user_anticipation = {}
    for contest, stats in contest_users.items():
        if name in contest_users[contest]:
            # print(f"# {contest} -> {contest_users[contest][name]}")
            user_anticipation[contest] = contest_users[contest][name]
    user_sorted = sorted(user_anticipation.items(), key=lambda kvp: -kvp[1])
    for contest, points in user_sorted:
        print(f"#  {contest} -> {points}")
