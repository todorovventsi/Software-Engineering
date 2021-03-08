from statistics import mean


students_number = int(input())
student_register = {}

for _ in range(students_number):
    student_name = input()
    student_grade = float(input())
    if student_name not in student_register:
        student_register[student_name] = []
    student_register[student_name].append(student_grade)

student_register = {name: grades for name, grades in student_register.items() if mean(grades) >= 4.5}
student_register = dict(sorted(student_register.items(), key=lambda item: -mean(item[1])))
for student, grade in student_register.items():
    print(f"{student} -> {mean(grade):.2f}")
