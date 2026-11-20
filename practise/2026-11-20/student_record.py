# exercise 8: student record tupple 
student = ("BSIT-12", "Sara", 88) 
class_name, student_name, marks = student
print("Class Name:", class_name)
print("Student Name:", student_name)
print("Marks:", marks)
# student.append(95)
# Traceback (most recent call last):
#   File "D:\STP\bootcamp\number and string\practise\2026-11-20\main.py", line 105, in <module>
#     student.append(95)
#     ^^^^^^^^^^^^^^
# AttributeError: 'tuple' object has no attribute 'append

# change the tupple into list and then append the marks
student_list = list(student)
student_list.append(95)
print("Updated student record:", student_list)

# now move back list to tupple
student = tuple(student_list)
print("Updated student record as tuple:", student)
