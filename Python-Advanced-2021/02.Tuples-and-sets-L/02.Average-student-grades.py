from statistics import mean

students_number = int(input())

students_register = {}

for _ in range(students_number):
    student_name, grade = input().split()
    if student_name not in students_register:
        students_register[student_name] = []
    students_register[student_name].append(float(grade))

for student, grades in students_register.items():
    print(f"{student} ->", end=" ")
    [print(f"{grade:.2f}", end=" ") for grade in grades]
    print(f"(avg: {mean(grades):.2f})")

