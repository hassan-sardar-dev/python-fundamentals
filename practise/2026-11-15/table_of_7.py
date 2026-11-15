"""Task 3 — Table of 7 (List comprehension).

Use a list comprehension to make [7, 14, ..., 70]

Run it with:
    python3 table_of_7.py
"""

# A list comprehension builds a list in one line:
# [expression for item in range(...)]
# Here: 7 * i, for i = 1, 2, ..., 10
table_of_7 = [7 * i for i in range(1, 11)]

print("Table of 7:", table_of_7)

# The same thing written as a normal loop, for comparison:
table_loop = []
for i in range(1, 11):
    table_loop.append(7 * i)
print("Same with a loop:", table_loop)
print("Both are equal:", table_of_7 == table_loop)
