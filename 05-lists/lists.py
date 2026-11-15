"""Lesson 05 - Lists.

Run: python3 lists.py
No input() here, so it runs start to finish without stopping.
"""

print("--- 1. What is a list? ---")
fruits = ["apple", "banana", "mango", "apple"]
print(fruits)
print(type(fruits))
print(len(fruits))
numbers = [1, 2, 3, 4, 5]
print(numbers)
empty = []
print(empty)

print("--- 2. Indexing ---")
fruits = ["apple", "banana", "mango", "orange"]
print(fruits[0])
print(fruits[1])
print(fruits[-1])
print(fruits[-2])

print("--- 3. Slicing ---")
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[:])
print(numbers[::2])
print(numbers[::-1])

print("--- 4. len(), in, not in ---")
fruits = ["apple", "banana", "mango"]
print(len(fruits))
print("banana" in fruits)
print("grapes" in fruits)
print("grapes" not in fruits)

print("--- 5. Changing items ---")
fruits = ["apple", "banana", "mango"]
fruits[1] = "grapes"
print(fruits)
fruits[0:2] = ["kiwi", "pear"]
print(fruits)

print("--- 6. Adding items: append, extend, insert ---")
fruits = ["apple", "banana"]
fruits.append("mango")
print(fruits)
fruits.extend(["kiwi", "pear"])
print(fruits)
fruits.insert(1, "grapes")
print(fruits)
# append() with a list adds ONE item (a list inside a list):
fruits2 = ["apple"]
fruits2.append(["banana", "mango"])
print(fruits2)

print("--- 7. Removing items: remove, pop, clear, del ---")
fruits = ["apple", "banana", "mango", "banana"]
fruits.remove("banana")
print(fruits)
last = fruits.pop()
print(last)
print(fruits)
first = fruits.pop(0)
print(first)
print(fruits)
del fruits[0]
print(fruits)
fruits = ["apple", "banana"]
fruits.clear()
print(fruits)

print("--- 8. Finding items: index, count ---")
fruits = ["apple", "banana", "mango", "apple"]
print(fruits.index("mango"))
print(fruits.index("apple"))
print(fruits.count("apple"))
print(fruits.count("kiwi"))

print("--- 9. Sorting and reversing ---")
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers.reverse()
print(numbers)
names = ["Hassan", "Ali", "Sara"]
print(sorted(names))
print(names)

print("--- 10. Concatenation and repetition ---")
a = [1, 2, 3]
b = [4, 5]
print(a + b)
print(a * 3)

print("--- 11. Copying vs aliasing ---")
list1 = [1, 2, 3]
list2 = list1  # alias, NOT a copy
list2.append(4)
print(list1)
print(list2)
list1 = [1, 2, 3]
list2 = list1.copy()
list3 = list(list1)
list4 = list1[:]
list2.append(4)
print(list1)
print(list2)
print(list3)
print(list4)

print("--- 12. Nested lists ---")
students = [["Hassan", 85], ["Ali", 90], ["Sara", 78]]
print(students[0])
print(students[0][0])
print(students[1][1])
print(students[2][0])

print("--- 13. Looping through a list (preview) ---")
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

print("--- 14. List comprehension ---")
squares = []
for n in [1, 2, 3, 4, 5]:
    squares.append(n * n)
print(squares)
squares = [n * n for n in [1, 2, 3, 4, 5]]
print(squares)
evens = [n for n in [1, 2, 3, 4, 5, 6] if n % 2 == 0]
print(evens)
names = ["hassan", "ali", "sara"]
upper_names = [name.upper() for name in names]
print(upper_names)

print("--- 15. Practical example: student marks ---")
marks = [85, 90, 78, 92, 88]
print("Marks:", marks)
print("Total:", sum(marks))
print("Average:", sum(marks) / len(marks))
print("Highest:", max(marks))
print("Lowest:", min(marks))
marks.append(95)
marks.sort(reverse=True)
print("Sorted:", marks)
print("Top score:", marks[0])

print("--- 16. Practical example: shopping list ---")
shopping = ["milk", "bread", "eggs"]
shopping.append("butter")
shopping.remove("bread")
print(shopping)
print("Items:", len(shopping))

print("--- 17. Common mistakes (shown safely) ---")
fruits = ["apple", "banana", "mango"]
try:
    print(fruits[4])
except IndexError as e:
    print("IndexError:", e)
try:
    fruits.remove("kiwi")
except ValueError as e:
    print("ValueError:", e)
numbers = [3, 1, 2]
result = numbers.sort()
print(numbers)
print(result)
