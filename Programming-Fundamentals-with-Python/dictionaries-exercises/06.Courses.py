courses_register = {}

data = input()

while not data == "end":
    course_name, student_name = data.split(" : ")
    if course_name not in courses_register:
        courses_register[course_name] = []
    courses_register[course_name].append(student_name)

    data = input()

courses_register = dict(sorted(courses_register.items(), key=lambda item: -len(item[1])))
for course in courses_register:
    courses_register[course].sort()
    print(f"{course}: {len(courses_register[course])}")
    for student in courses_register[course]:
        print(f"-- {student}")
