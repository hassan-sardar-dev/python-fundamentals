"""Lesson 03 - Numbers.

Run: python3 numbers.py
No input() here, so it runs start to finish without stopping.
This file fixes and expands Hassan's original number.py
(the old comment said "mehtods" - the correct spelling is "methods").
"""

import math
import random

print("--- 1. int, float, complex ---")
a = 10
b = 3.5
c = 2 + 3j
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(10 + 3.5, type(10 + 3.5))

print("--- 2. Arithmetic operators ---")
print(5 + 3)
print(5 - 3)
print(5 * 3)
print(5 / 2)
print(5 // 2)
print(5 % 2)
print(2 ** 3)
print(10 % 3)
print(-7 // 2)
print("Is 10 even?", 10 % 2 == 0)

print("--- 3. Precedence ---")
print(2 + 3 * 4)
print((2 + 3) * 4)
print(2 ** 3 ** 2)
print(10 - 4 - 3)

print("--- 4. Built-in functions ---")
print(round(10.5))
print(round(10.6))
print(round(3.14159, 2))
print(abs(-7))
print(min(3, 1, 9))
print(max(3, 1, 9))
print(pow(2, 3))
print(sum([1, 2, 3, 4]))

print("--- 5. The math module ---")
# 10 methods of numbers: round, floor, ceil, abs, pow, sqrt, log, sin, cos, pi
num = 100
print(type(num))
num2 = 1999
print(type(num2))
print(num + num2)

num3 = 10.5
print(round(num3))

num4 = 12.3
print(math.floor(num4))
print(math.ceil(num4))
print(abs(num4))
print(pow(num4, 2))
print(math.sqrt(num4))
print(math.log(num4))
print(math.log10(100))
print(math.sin(0))
print(math.cos(0))
print(math.pi)
print(math.e)

print("--- 6. The random module ---")
data = [1, 2, 3, 4, 5]
print(random.choice(data))
print(random.randint(1, 10))
print(random.randrange(0, 10, 2))
print(random.random())
print(random.uniform(1, 5))

print("--- 7. Formatting numbers ---")
price = 49.99
print(f"Price: {price}")
print(f"Price: {price:.2f}")
print(f"Price: {price:.0f}")
print(f"Big number: {1000000:,}")
print(f"Percent: {0.856:.1%}")
print(f"Pi: {3.14159:.3f}")

print("--- 8. Common mistakes: float precision ---")
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
print(round(0.1 + 0.2, 2))
print(abs((0.1 + 0.2) - 0.3) < 0.0001)
print(int(3.9))
print(round(3.9))
