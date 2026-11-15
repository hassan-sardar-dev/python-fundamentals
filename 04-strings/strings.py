"""Lesson 04 - Strings.

Run: python3 strings.py
No input() here, so it runs start to finish without stopping.
This file fixes and expands Hassan's original string.py.
"""

print("--- 1. Single, double, triple quotes ---")
single = 'hello'
double = "hello"
triple = """hello"""
print(single, double, triple)
sentence = "It's a nice day"
print(sentence)
message = """Hello,
this is line two,
and this is line three."""
print(message)

print("--- 2. Indexing ---")
word = "Python"
print(word[0])
print(word[1])
print(word[-1])
print(word[-2])

print("--- 3. Slicing ---")
line = "This is a sample line of text"
print(line[0])
print(line[5:10])
print(line[-5:])
print(line[:4])
print(line[5:])
print(line[:])
print(line[::2])
print(line[::-1])

print("--- 4. Concatenation and repetition ---")
first = "Hassan"
last = "Sardar"
print(first + " " + last)
print("Ha" * 3)
print("-" * 20)
age = 20
print("Age: " + str(age))
print(f"Age: {age}")

print("--- 5. len(), in, not in ---")
name = "Hassan"
print(len(name))
print("H" in name)
print("z" in name)
print("z" not in name)
print("ass" in name)

print("--- 6. f-strings ---")
name = "Hassan"
age = 20
print(f"My name is {name} and I am {age} years old.")
print(f"Next year I will be {age + 1}.")
print(f"My name in upper case is {name.upper()}.")

print("--- 7. Escape characters ---")
print("Hello\nWorld")
print("Name:\tHassan")
print("C:\\Users\\Hassan")
print('He said "Hi"')
print("It's fine")

print("--- 8. Immutability ---")
word = "hello"
print(word.upper())
print(word)
word = word.upper()
print(word)

print("--- 9. Case methods ---")
name = 'my name is hassan'
print(name)
print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())
print("HELLO".casefold())

print("--- 10. Strip methods ---")
print("  hi  ".strip())
print("  hi  ".lstrip())
print("  hi  ".rstrip())

print("--- 11. Split and join ---")
print(name.split(" "))
print("a b c".split())
print("a,b,c".rsplit(",", 1))
print("-".join(["a", "b"]))
print(", ".join(["apple", "banana", "mango"]))

print("--- 12. Search and replace ---")
print(line.replace("sample", "test"))
print(line.find("line"))
print(line.index("line"))
print(line.count("is"))
print("hello".startswith("he"))
print("hello".endswith("lo"))
print("hello".find("z"))

print("--- 13. Check methods (True/False) ---")
print("abc".isalpha())
print("ab1".isalpha())
print("123".isdigit())
print("12a".isdigit())
print("abc123".isalnum())
print("ab c".isalnum())
print("   ".isspace())
print(" a ".isspace())

print("--- 14. Hassan's first string examples ---")
age = 20
print(f'My name is {name} and I am {age} years old')
print(line[0])
print(line[5:10])
print(line[-5:])
print(line.replace("sample", "test"))
print(line.find("line"))
print(line.count("is"))

print("--- 15. Username check (from main.py / login.py) ---")


def username(name):
    if name == "Hassan":
        return "This is valid username"
    else:
        return "This is not a valid username"


print(username("Hassan"))
print(username("Ali"))


def check_username(name):
    return name.strip().title() == "Hassan"


print(check_username("  hassan  "))
print(check_username("Ali"))
