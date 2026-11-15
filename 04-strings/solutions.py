"""Lesson 04 - Strings: Solutions.

Run: python3 solutions.py
"""

print("--- Exercise 1: First and last letters ---")
word = "Python"
print(word[0])
print(word[-1])
print(len(word))

print("--- Exercise 2: Slice a sentence ---")
sentence = "I am learning Python"
print(sentence[:4])
print(sentence[-6:])
print(sentence[::-1])

print("--- Exercise 3: Clean up user input ---")
messy = "   hello WORLD   "
clean = messy.strip().lower()
print(clean)
print(clean.title())

print("--- Exercise 4: Split and join ---")
sentence = "apple banana mango orange"
fruits = sentence.split()
print(fruits)
print(" - ".join(fruits))

print("--- Exercise 5: Username checker ---")


def check_username(name):
    return name.strip().title() == "Hassan"


print(check_username("  hassan  "))
print(check_username("Hassan"))
print(check_username("Ali"))
