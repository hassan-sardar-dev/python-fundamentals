"""Lesson 02 - Data Types.

Run: python3 data_types.py
No input() here, so it runs start to finish without stopping.
"""

print("--- 1. type() ---")
print(type(10))
print(type(3.5))
print(type("Hassan"))
print(type(True))
print(type(None))

print("--- 2. int, float, str, bool ---")
age = 20
price = 99.99
name = "Hassan"
is_student = True
print(age, type(age))
print(price, type(price))
print(name, type(name))
print(is_student, type(is_student))

print("--- 3. NoneType ---")
result = None
print(result)
print(type(result))

print("--- 4. list, tuple, set, dict ---")
fruits = ["apple", "banana", "mango"]
point = (10, 20)
unique_numbers = {1, 2, 2, 3}
person = {"name": "Hassan", "age": 20}
print(fruits, type(fruits))
print(point, type(point))
print(unique_numbers, type(unique_numbers))
print(person, type(person))
print(fruits[0])
print(point[1])
print(person["name"])

print("--- 5. isinstance() ---")
print(isinstance(10, int))
print(isinstance(3.5, int))
print(isinstance("Hi", str))
print(isinstance(True, bool))
print(isinstance([1, 2], list))
print(isinstance({"a": 1}, dict))

print("--- 6. Conversion: int(), float(), str(), bool() ---")
print(int("42"))
print(int(3.9))
print(float(10))
print(str(100))
print(bool(1))
print(bool(0))
print(bool(""))
print(int(float("3.5")))

print("--- 7. Mutable vs immutable ---")
numbers = [1, 2, 3]
numbers[0] = 99
print(numbers)  # list changed in place: mutable
name = "Hassan"
name = "hassan"  # new string, old one not changed: immutable
print(name)

print("--- 8. Truthy and falsy ---")
print(bool(0), bool(""), bool([]), bool(None))
print(bool(1), bool("hi"), bool([0]))
