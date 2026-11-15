"""Lesson 01 - Variables.

Run: python3 variables.py
No input() here, so it runs start to finish without stopping.
"""

print("--- 1. What is a variable ---")
name = "Hassan"
age = 20
print(name)
print(age)

print("--- 2. Using variables ---")
city = "Lahore"
price = 150
print(city)
print("Price:", price)

apples = 5
oranges = 3
total = apples + oranges
print(total)
print(f"I have {total} fruits.")

print("--- 3. Naming rules ---")
user_name = "Hassan"
age2 = 20
_private = 1
print(user_name, age2, _private)
# Case matters: these are three different variables.
Age = 30
AGE = 40
print(age, Age, AGE)

print("--- 4. Multiple assignment ---")
x, y, z = 1, 2, 3
print(x, y, z)
a = b = c = 0
print(a, b, c)

print("--- 5. Swapping values ---")
a = 5
b = 10
print("Before swap:", a, b)
a, b = b, a
print("After swap:", a, b)

print("--- 6. Reassigning a variable ---")
score = 10
print(score)
score = 25
print(score)
score = score + 5
print(score)

print("--- 7. Dynamic typing ---")
data = 100
print(data, type(data))
data = "hello"
print(data, type(data))
data = 3.5
print(data, type(data))

print("--- 8. Constants (UPPER_CASE) ---")
PI = 3.14159
MAX_USERS = 100
print(PI)
print(MAX_USERS)

print("--- 9. Variables in print() and f-strings ---")
name = "Hassan"
age = 20
print("My name is", name, "and I am", age, "years old.")
print(f"My name is {name} and I am {age} years old.")
print(f"Next year {name} will be {age + 1}.")

print("--- 10. input() example (shown, not run) ---")
print('name = input("Enter your username: ")')
print('print(f"Hello, {name}!")')
print("Try it in login.py at the repo root: python3 login.py")
