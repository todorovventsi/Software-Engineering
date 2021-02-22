import math
import sys

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

max_student_score = 0
best_student_attendances = 0

for _ in range(number_of_students):
    student_attendances = int(input())
    student_score = (student_attendances / number_of_lectures) * (5 + additional_bonus)
    if student_score > max_student_score:
        max_student_score = student_score
        best_student_attendances = student_attendances

print(f"Max Bonus: {math.ceil(max_student_score)}.")
print(f"The student has attended {best_student_attendances} lectures.")
