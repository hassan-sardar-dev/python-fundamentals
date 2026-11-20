# solutions 03
import math
import random

# question 1
a = 17
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** 2)

# question 2
radius = 7
area = math.pi * radius ** 2
print(round(area, 2))

# question 3
number = 29
print(number % 2 == 0)
number = 30
print(number % 2 == 0)

# question 4
roll = random.randint(1, 6)
print("You rolled a", roll)
fruits = ["apple", "banana", "mango", "orange"]
print(random.choice(fruits))

# question 5
total = 3 * 49.99 + 2 * 129.50
print("Total:", round(total, 2))
