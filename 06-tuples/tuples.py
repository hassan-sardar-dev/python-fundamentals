"""Lesson 06 - Tuples.

Run: python3 tuples.py
No input() here, so it runs start to finish without stopping.
"""

print("--- 1. What is a tuple? ---")
point = (10, 20)
print(point)
print(type(point))
print(len(point))
colours = ("red", "green", "blue", "red")
print(colours)
student = ("Hassan", 20, 85.5)
print(student)

print("--- 2. Creating tuples: the tricky cases ---")
empty = ()
print(empty)
numbers = tuple([1, 2, 3])
print(numbers)
one = (5,)
print(one)
print(type(one))
not_a_tuple = (5)
print(not_a_tuple)
print(type(not_a_tuple))
point = 10, 20
print(point)
print(type(point))

print("--- 3. Indexing ---")
colours = ("red", "green", "blue")
print(colours[0])
print(colours[1])
print(colours[-1])
print(colours[-2])

print("--- 4. Slicing ---")
numbers = (10, 20, 30, 40, 50, 60)
print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[:])
print(numbers[::2])
print(numbers[::-1])

print("--- 5. len(), in, not in ---")
colours = ("red", "green", "blue")
print(len(colours))
print("green" in colours)
print("yellow" in colours)
print("yellow" not in colours)

print("--- 6. Immutability ---")
point = (10, 20)
try:
    point[0] = 30
except TypeError as e:
    print("TypeError:", e)
try:
    point.append(30)
except AttributeError as e:
    print("AttributeError:", e)
point = (30, 20)
print(point)
# A list inside a tuple can still change, but the tuple itself cannot:
data = (1, [2, 3])
data[1].append(4)
print(data)

print("--- 7. Unpacking ---")
student = ("Hassan", 20, 85)
name, age, marks = student
print(name)
print(age)
print(marks)
a = 5
b = 10
a, b = b, a
print(a, b)
numbers = (1, 2, 3, 4, 5)
first, second, *rest = numbers
print(first)
print(second)
print(rest)

print("--- 8. Tuple methods: count, index ---")
colours = ("red", "green", "blue", "red")
print(colours.count("red"))
print(colours.count("yellow"))
print(colours.index("green"))
print(colours.index("red"))

print("--- 9. Tuple vs list ---")
shopping = ["milk", "bread"]
shopping.append("eggs")
print(shopping)
point = (10, 20)
print(point)
print("List:", type(shopping), "- mutable, many methods")
print("Tuple:", type(point), "- immutable, only count and index")

print("--- 10. Nested tuples ---")
students = (("Hassan", 85), ("Ali", 90), ("Sara", 78))
print(students[0])
print(students[0][0])
print(students[1][1])
for name, marks in students:
    print(name, marks)

print("--- 11. Returning multiple values from a function ---")


def get_student():
    return ("Hassan", 20, 85)


name, age, marks = get_student()
print(name)
print(age)
print(marks)

print("--- 12. Converting between lists and tuples ---")
fruits_list = ["apple", "banana", "mango"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)
names_tuple = ("Hassan", "Ali", "Sara")
names_list = list(names_tuple)
print(names_list)
names_list.append("Zain")
print(names_list)

print("--- 13. Practical example: a student record ---")
student = ("Hassan", 20, 85)
name, age, marks = student
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Marks: {marks}")
point = (10, 20)
x, y = point
print(f"Point is at x={x}, y={y}")
class_marks = (("Hassan", 85), ("Ali", 90), ("Sara", 78))
print("Students:", len(class_marks))
print("Top student:", class_marks[1])
