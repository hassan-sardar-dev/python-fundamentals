# conditionals and loops

# comparison
age = 20
print(age >= 18)
print(age == 20)
print(age < 18)
name = "Hassan"
print(name == "Hassan")
print(name != "Ali")

# and or not
has_ticket = True
print(age >= 18 and has_ticket)
print(age < 18 or has_ticket)
print(not has_ticket)
fruits = ["apple", "banana", "mango"]
print("mango" in fruits)
print("orange" not in fruits)
print("a" in "Hassan")

# if elif else
marks = 85
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"
print(grade)

# nested if
is_logged_in = True
is_admin = False
if is_logged_in:
    if is_admin:
        print("Welcome, admin.")
    else:
        print("Welcome, user.")
else:
    print("Please log in first.")

# one line if else
status = "adult" if age >= 18 else "minor"
print(status)

# empty is false
username = ""
if username:
    print("Hello,", username)
else:
    print("No name given.")
items = ["apple", "banana"]
if items:
    print("We have", len(items), "items.")

# for loop
for fruit in fruits:
    print(fruit)
for letter in "Hassan":
    print(letter)

# range
for n in range(5):
    print(n)
for n in range(1, 6):
    print(n)
for n in range(0, 11, 2):
    print(n)

# loop with number
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)

# total with loop
numbers = [1, 2, 3, 4, 5]
total = 0
for n in numbers:
    total = total + n
print(total)

# even numbers
evens = []
for n in [1, 2, 3, 4, 5, 6, 7, 8]:
    if n % 2 == 0:
        evens.append(n)
print(evens)

# while loop
count = 1
while count <= 5:
    print(count)
    count = count + 1

# break and continue
for n in range(1, 11):
    if n == 6:
        break
    print(n)
for n in range(1, 6):
    if n == 3:
        continue
    print(n)
for n in range(3):
    pass
print("Loop finished")

# search in list
names = ["Ali", "Sara", "Bilal"]
for person in names:
    if person == "Hassan":
        print("Found Hassan!")
        break
else:
    print("Hassan is not in the list.")

# table
for row in range(1, 4):
    for col in range(1, 4):
        print(row, "x", col, "=", row * col)
