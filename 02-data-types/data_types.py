# data types

# type
print(type(10))
print(type(3.5))
print(type("Hassan"))
print(type(True))
print(type(None))

# int, float, str, bool
age = 20
price = 99.99
name = "Hassan"
is_student = True
print(age, type(age))
print(price, type(price))
print(name, type(name))
print(is_student, type(is_student))

# none
result = None
print(result)
print(type(result))

# list, tuple, set, dict
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

# isinstance
print(isinstance(10, int))
print(isinstance(3.5, int))
print(isinstance("Hi", str))
print(isinstance(True, bool))
print(isinstance([1, 2], list))
print(isinstance({"a": 1}, dict))

# conversion
print(int("42"))
print(int(3.9))
print(float(10))
print(str(100))
print(bool(1))
print(bool(0))
print(bool(""))
print(int(float("3.5")))

# mutable vs immutable
numbers = [1, 2, 3]
numbers[0] = 99
print(numbers)
name = "Hassan"
name = "hassan"
print(name)

# truthy and falsy
print(bool(0), bool(""), bool([]), bool(None))
print(bool(1), bool("hi"), bool([0]))
