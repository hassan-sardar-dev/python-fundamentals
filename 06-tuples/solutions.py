"""Lesson 06 - Tuples: Solutions.

Run: python3 solutions.py
"""

print("--- Exercise 1: Make a tuple ---")
colours = ("red", "green", "blue")
print(colours)
print(colours[0])
print(colours[-1])
print(len(colours))

print("--- Exercise 2: Unpack a student record ---")
student = ("Hassan", 20, 85)
name, age, marks = student
print(name)
print(age)
print(marks)
a = 5
b = 10
a, b = b, a
print(a, b)

print("--- Exercise 3: Count and find ---")
letters = ("a", "b", "a", "c", "a")
print(letters.count("a"))
print(letters.index("c"))
print("d" in letters)

print("--- Exercise 4: List to tuple and back ---")
fruits = ["apple", "banana", "mango"]
fruits_tuple = tuple(fruits)
print(fruits_tuple)
fruits_list = list(fruits_tuple)
fruits_list.append("orange")
print(fruits_list)

print("--- Exercise 5: A class record ---")
class_marks = (("Hassan", 85), ("Ali", 90), ("Sara", 78))
print("Students:", len(class_marks))
print(class_marks[1][0], class_marks[1][1])
highest = max(class_marks[0][1], class_marks[1][1], class_marks[2][1])
print("Highest marks:", highest)
