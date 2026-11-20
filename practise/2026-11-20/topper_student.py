# excercise 10 
students = [("Ali", 85), ("Sara", 92), ("Ahmed", 76), ("Hina", 64)] 
print(students)
for student in students:
    print(f"Name: {student[0]}, Marks: {student[1]}")
max = 0
for student in students:
    if student[1] > max:
        max = student[1]
        top_student = student[0]
print(f"Topper: {top_student} with marks: {max}")

for i in students:
    if i[1] >= 70:
        print(f"{i[0]}  {i[1]}")
