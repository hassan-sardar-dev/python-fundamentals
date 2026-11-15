"""Lesson 02 - Data Types: Solutions.

Run: python3 solutions.py
"""

print("--- Exercise 1: What type is it? ---")
print(type(42))
print(type(3.14))
print(type("Python"))
print(type(True))
print(type(None))
print(type([1, 2]))
print(type((1, 2)))
print(type({"a": 1}))

print("--- Exercise 2: Convert a string age ---")
age_text = "25"
age = int(age_text)
print(age + 5)
age_str = str(age + 5)
print(type(age_str))

print("--- Exercise 3: isinstance() checks ---")
score = 95
name = "Hassan"
price = 49.99
active = False
print(isinstance(score, int))
print(isinstance(name, str))
print(isinstance(price, int))
print(isinstance(active, bool))

print("--- Exercise 4: Mutable vs immutable ---")
colours = ["red", "green", "blue"]
colours[1] = "yellow"
print(colours)
word = "hello"
word_upper = word.upper()
print(word)
print(word_upper)

print("--- Exercise 5: Truthy or falsy? ---")
print(bool(0))        # False — zero is falsy
print(bool(1))        # True — non-zero number is truthy
print(bool(""))       # False — empty string is falsy
print(bool("hello"))  # True — non-empty string is truthy
print(bool([]))       # False — empty list is falsy
print(bool([0]))      # True — a list with an item is truthy
print(bool(None))     # False — None is falsy
