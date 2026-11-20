# solutions 06

# question 1
colours = ("red", "green", "blue")
print(colours)
print(colours[0])
print(colours[-1])
print(len(colours))

# question 2
student = ("Hassan", 20, 85)
name, age, marks = student
print(name)
print(age)
print(marks)
a = 5
b = 10
a, b = b, a
print(a, b)

# question 3
letters = ("a", "b", "a", "c", "a")
print(letters.count("a"))
print(letters.index("c"))
print("d" in letters)

# question 4
fruits = ["apple", "banana", "mango"]
fruits_tuple = tuple(fruits)
print(fruits_tuple)
fruits_list = list(fruits_tuple)
fruits_list.append("orange")
print(fruits_list)

# question 5
class_marks = (("Hassan", 85), ("Ali", 90), ("Sara", 78))
print("Students:", len(class_marks))
print(class_marks[1][0], class_marks[1][1])
highest = class_marks[0][1]
for s in class_marks:
    if s[1] > highest:
        highest = s[1]
print("Highest marks:", highest)
