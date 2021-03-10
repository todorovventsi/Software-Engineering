command = input()
courses = {}

while not command == "end":
    course_name, student = command.split(": ")
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student)

    command = input()


courses = dict(sorted(courses.items(), key=lambda kvp: -len(kvp[1])))

for course in courses:
    courses[course].sort()
    print(f"{course}: {len(courses[course])}")
    for student in courses[course]:
        print(f"-- {student}")
