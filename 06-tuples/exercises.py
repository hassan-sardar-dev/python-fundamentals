"""Lesson 06 - Tuples: Exercises.

Run: python3 exercises.py
Try each exercise yourself. Do NOT look at solutions.py until you have tried.
"""

print("--- Exercise 1: Make a tuple ---")
# Create a tuple called colours with "red", "green", "blue".
# Print the whole tuple, then print the first item, the last item,
# and the number of items (use indexing and len()).


print("--- Exercise 2: Unpack a student record ---")
# Create student = ("Hassan", 20, 85).
# Unpack it into three variables called name, age, and marks,
# then print each one on its own line.
# Then swap two numbers a = 5 and b = 10 using tuple unpacking
# (a, b = b, a) and print them — they should be 10 and 5.


print("--- Exercise 3: Count and find ---")
# Create letters = ("a", "b", "a", "c", "a").
# Print how many times "a" appears, and print the index of "c".
# Then check if "d" is in the tuple and print the answer (False).


print("--- Exercise 4: List to tuple and back ---")
# Start with fruits = ["apple", "banana", "mango"] (a list).
# Convert it to a tuple called fruits_tuple and print it.
# Then convert fruits_tuple back to a list, add "orange" to the list,
# and print the final list.
# It should end as: ['apple', 'banana', 'mango', 'orange']


print("--- Exercise 5: A class record ---")
# Create a tuple of tuples called class_marks:
# (("Hassan", 85), ("Ali", 90), ("Sara", 78))
# Print the number of students, print the second student's name
# and marks, and print the highest marks in the class (90).
# (Hint: the marks are at index [1] of each student tuple,
#  so the highest is max(class_marks[0][1], class_marks[1][1],
#  class_marks[2][1]).)
