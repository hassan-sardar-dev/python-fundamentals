# #  question 1) # print the first , last and the 3 from the middle cities 
# cities = ["Lahore", "Karachi", "Multan", "Quetta", "Peshawar"] 
# print(cities[0], cities[-1], cities[1:4])  
# # reverse cities  
# cities.reverse()
# print(cities)

# # question 2: find total , average , highest and lowest marks 
# # total 
# marks = [78, 92, 65, 88, 54]
# sum = 0
# for mark in marks:
#     sum += mark
# print("Total marks:", sum)
# # average 
# marks_two = [78, 92, 65, 88, 54]
# sum2 = 0
# for mark in marks_two:
#     sum2 += mark
# average = sum2 / len(marks_two)
# print("Average marks:", average)

# # largest 
# marks_three = [78, 92, 65, 88 , 54]
# max = marks_three[0]
# for i in marks_three:
#     if i > max:
#         max = i
# print('highest marks', max)

# # smallest 
# marks_four = [78 , 92 , 65, 88 , 54]
# min = marks_four[0]
# for i in marks_four:
#     if i < min:
#         min = i
# print("lowest number" , min )

# # greather then 70
# marks_five = [78 , 92 , 65, 88 , 54]
# greater = marks_five[0]
# for i in marks_five:
#     if i >= 70:
#       print('greater', i)
# question  3 shopping list 
# # shopping list 
# shopping_list = ["bread", "milk", "eggs"]
# shopping_list.append('rice')
# print(shopping_list)
# shopping_list.insert(1, 'suggar')
# print(shopping_list)
# shopping_list.remove('milk')
# print(shopping_list)
# shopping_list.pop()
# print(shopping_list)



# level 2 excerse 4 remove the duplicates from the list

original_list = [3, 1, 3, 2, 1, 5]
unique_list = []

for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)

# exercise 5: find even and odd numbers from the list
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
even_num =[]
odd_num = []
for num in num_list:
    if num % 2 == 0:
        even_num.append(num)
        
    else:
        odd_num.append(num)
print("Even numbers:", even_num)
print("Odd numbers:", odd_num)

# exercise 6: reverse the list
r = [1, 2, 3, 4, 5] 
y=r[::-1]
print(y)

# excercise 7: copy of the list 
a = [1, 2, 3]
b = a
c = a.copy()
a.append(4)
print("a:", a)
print("b:", b)
print("c:", c)
# b changed because it is a shallow copy of a, while c is a deep copy and remains unchanged.


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

# excercise 9: vote counter 
votes = ("A", "B", "A", "C", "A", "B") 
print("Votes for A:", votes.count("A"))
print("Votes for B:", votes.count("B"))
print("Votes for C:", votes.count("C"))
print("Index of first C:", votes.index("C"))

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

# excerise 11 second largest number from the list
scores = [45, 82, 67, 91, 73] 
maxnumber = 0
secondmax = 0
for i in scores:
    if i > maxnumber:
        secondmax = maxnumber
        maxnumber = i
        print("max", maxnumber) # it will takes the first number on 0 index as max and then it will moves on ward  and find more max then this number
    elif i > secondmax and i != maxnumber:
        secondmax = i
        print("secondmax", secondmax) # it will takes the second largest number and then it will moves on ward  and find more second largest then this number
print("Second largest score:", secondmax)