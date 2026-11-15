"""Lesson 01 - Variables: Solutions.

Run: python3 solutions.py
"""

print("--- Exercise 1: Your introduction ---")
your_name = "Hassan"
your_age = 20
print(f"My name is {your_name} and I am {your_age} years old.")

print("--- Exercise 2: Simple maths with variables ---")
a = 12
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)

print("--- Exercise 3: Swap two values ---")
x = 7
y = 9
print("Before swap:", x, y)
x, y = y, x
print("After swap:", x, y)

print("--- Exercise 4: Reassign and update ---")
score = 0
print(score)
score = score + 10
print(score)
score += 5
print(score)

print("--- Exercise 5: A small shop bill ---")
pen_price = 50
notebook_price = 120
pen_qty = 2
notebook_qty = 3
total = pen_price * pen_qty + notebook_price * notebook_qty
print(f"Total bill: {total}")
