# 02 — Data Types

## What is a data type?

Every value in Python has a type. The type tells Python what the value is
and what you can do with it. `10` is a number you can add; `"10"` is text
you can print but not add like a number.

Use `type()` to check a value's type:

```python
print(type(10))        # <class 'int'>
print(type(3.5))       # <class 'float'>
print(type("Hassan"))  # <class 'str'>
print(type(True))      # <class 'bool'>
```

## The main types

| Type | What it is | Example |
|---|---|---|
| `int` | Whole number | `20`, `-5`, `0` |
| `float` | Number with a decimal point | `3.5`, `-0.25`, `2.0` |
| `str` | Text (string) | `"Hassan"`, `'hello'` |
| `bool` | True or False | `True`, `False` |
| `NoneType` | No value / nothing | `None` |
| `list` | Ordered, changeable collection | `[1, 2, 3]`, `["a", "b"]` |
| `tuple` | Ordered, unchangeable collection | `(1, 2, 3)`, `("a", "b")` |
| `set` | Unordered collection, no duplicates | `{1, 2, 3}` |
| `dict` | Key-value pairs | `{"name": "Hassan", "age": 20}` |

## int, float, str, bool

```python
age = 20            # int
price = 99.99       # float
name = "Hassan"     # str
is_student = True   # bool

print(type(age), type(price), type(name), type(is_student))
```

## NoneType — `None`

`None` means "no value yet". It is often used as a starting value, or as
the result of a function that returns nothing.

```python
result = None
print(result)        # None
print(type(result))  # <class 'NoneType'>
```

## list, tuple, set, dict

These hold more than one value. They are covered in depth in Lesson 07;
here is a first look:

```python
fruits = ["apple", "banana", "mango"]   # list — ordered, can change
point = (10, 20)                        # tuple — ordered, cannot change
unique_numbers = {1, 2, 2, 3}           # set — no duplicates: {1, 2, 3}
person = {"name": "Hassan", "age": 20}  # dict — keys and values

print(fruits[0])        # apple
print(point[1])         # 20
print(unique_numbers)   # {1, 2, 3}
print(person["name"])   # Hassan
```

## Checking a type with isinstance()

`isinstance()` checks whether a value is of a given type. It returns
`True` or `False` and is safer than comparing with `type()`:

```python
print(isinstance(10, int))       # True
print(isinstance(3.5, int))      # False
print(isinstance("Hi", str))     # True
print(isinstance(True, bool))    # True
print(isinstance([1, 2], list))  # True
```

## Converting between types

Use `int()`, `float()`, `str()`, and `bool()` to convert a value:

```python
print(int("42"))       # 42        (string -> int)
print(int(3.9))        # 3         (cuts off the decimal, does not round)
print(float(10))       # 10.0
print(str(100))        # "100"
print(bool(1))         # True
print(bool(0))         # False
print(bool(""))        # False
```

Watch out — converting text that is not a number fails:

```python
# int("hello")   # ValueError: invalid literal for int()
# int("3.5")     # ValueError — use float("3.5") first, then int()
print(int(float("3.5")))   # 3
```

`input()` always returns a string, so convert it before doing maths:

```python
# age = input("Enter your age: ")   # e.g. user types 20 -> "20"
# print(age + 1)                    # TypeError: "20" + 1
# print(int(age) + 1)               # 21 — correct
```

## Mutable vs immutable

- **Mutable** (can be changed after creation): `list`, `dict`, `set`
- **Immutable** (cannot be changed after creation): `int`, `float`, `str`,
  `bool`, `tuple`, `NoneType`

```python
# Mutable: a list can change
numbers = [1, 2, 3]
numbers[0] = 99
print(numbers)   # [99, 2, 3]

# Immutable: a string cannot change in place
name = "Hassan"
# name[0] = "h"   # TypeError — strings are immutable
name = "hassan"   # this is fine: it makes a NEW string and reassigns the name
print(name)       # hassan
```

## Truthy and falsy

In an `if` test, some values count as `False` (falsy) and everything else
counts as `True` (truthy):

```python
# Falsy values: False, 0, 0.0, "", [], {}, set(), None
print(bool(0))        # False
print(bool(""))       # False
print(bool([]))       # False
print(bool(None))     # False

# Truthy values: almost everything else
print(bool(1))        # True
print(bool("hi"))     # True
print(bool([0]))      # True — a list with one item, even if that item is 0
```

## Common mistakes

| Mistake | What happens |
|---|---|
| `"20" + 1` | `TypeError` — add a string and a number? Convert first: `int("20") + 1` |
| `int("3.5")` | `ValueError` — use `int(float("3.5"))` |
| Forgetting `input()` returns a string | Maths on it fails until you convert it |
| Changing a string in place | Strings are immutable — make a new string instead |

## Run it

```bash
python3 data_types.py
python3 exercises.py
python3 solutions.py
```

Next: [03 — Numbers](../03-numbers/README.md)
