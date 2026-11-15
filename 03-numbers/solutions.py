"""Lesson 03 - Numbers: Solutions.

Run: python3 solutions.py
"""

import math
import random

print("--- Exercise 1: Basic arithmetic ---")
a = 17
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** 2)

print("--- Exercise 2: Circle area ---")
radius = 7
area = math.pi * radius ** 2
print(round(area, 2))

print("--- Exercise 3: Even or odd? ---")
number = 29
print(number % 2 == 0)
number = 30
print(number % 2 == 0)

print("--- Exercise 4: Random dice roll ---")
roll = random.randint(1, 6)
print(f"You rolled a {roll}")
fruits = ["apple", "banana", "mango", "orange"]
print(random.choice(fruits))

print("--- Exercise 5: A shop total with formatting ---")
total = 3 * 49.99 + 2 * 129.50
print(f"Total: {total:.2f}")
