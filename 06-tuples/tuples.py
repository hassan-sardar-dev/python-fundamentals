# tuples

# what is tuple
point = (10, 20)
print(point)
print(type(point))
print(len(point))
colours = ("red", "green", "blue", "red")
print(colours)
student = ("Hassan", 20, 85.5)
print(student)

# one item tuple
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

# indexing
colours = ("red", "green", "blue")
print(colours[0])
print(colours[1])
print(colours[-1])
print(colours[-2])

# slicing
numbers = (10, 20, 30, 40, 50, 60)
print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[:])
print(numbers[::2])
print(numbers[::-1])

# len and in
colours = ("red", "green", "blue")
print(len(colours))
print("green" in colours)
print("yellow" in colours)
print("yellow" not in colours)

# cant change tuple
point = (10, 20)
# point[0] = 30, this will give error
point = (30, 20)
print(point)
# list inside tuple can change
data = (1, [2, 3])
data[1].append(4)
print(data)

# unpack
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

# count and index
colours = ("red", "green", "blue", "red")
print(colours.count("red"))
print(colours.count("yellow"))
print(colours.index("green"))
print(colours.index("red"))

# tuple vs list
shopping = ["milk", "bread"]
shopping.append("eggs")
print(shopping)
point = (10, 20)
print(point)
print("List:", type(shopping))
print("Tuple:", type(point))

# nested tuple
students = (("Hassan", 85), ("Ali", 90), ("Sara", 78))
print(students[0])
print(students[0][0])
print(students[1][1])
for name, marks in students:
    print(name, marks)

# function returns tuple
def get_student():
    return ("Hassan", 20, 85)

name, age, marks = get_student()
print(name)
print(age)
print(marks)

# list to tuple and back
fruits_list = ["apple", "banana", "mango"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)
names_tuple = ("Hassan", "Ali", "Sara")
names_list = list(names_tuple)
print(names_list)
names_list.append("Zain")
print(names_list)

# student record
student = ("Hassan", 20, 85)
name, age, marks = student
print("Name:", name)
print("Age:", age)
print("Marks:", marks)
point = (10, 20)
x, y = point
print("Point is at x=", x, "y=", y)
class_marks = (("Hassan", 85), ("Ali", 90), ("Sara", 78))
print("Students:", len(class_marks))
print("Top student:", class_marks[1])
