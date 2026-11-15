"""Lesson 05 - Lists: Solutions.

Run: python3 solutions.py
"""

print("--- Exercise 1: Make a fruit list ---")
fruits = ["apple", "banana", "mango", "orange"]
print(fruits)
print(fruits[0])
print(fruits[-1])
print(len(fruits))

print("--- Exercise 2: Add and remove items ---")
shopping = ["milk", "bread", "eggs"]
shopping.append("butter")
shopping.insert(1, "cheese")
shopping.remove("bread")
print(shopping)

print("--- Exercise 3: Sort, find, and count ---")
numbers = [5, 2, 9, 1, 7, 5, 2]
print(numbers.count(5))
print(numbers.index(9))
numbers.sort()
print(numbers)

print("--- Exercise 4: Student marks ---")
marks = [85, 90, 78, 92, 88]
print("Total:", sum(marks))
print("Average:", sum(marks) / len(marks))
print("Highest:", max(marks))
print("Lowest:", min(marks))
marks.append(95)
marks.sort(reverse=True)
print("Sorted:", marks)
print("Top mark:", marks[0])

print("--- Exercise 5: Squares with list comprehension ---")
squares = [n * n for n in [1, 2, 3, 4, 5]]
print(squares)
evens = [n for n in range(1, 11) if n % 2 == 0]
print(evens)
