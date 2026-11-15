# 01 — Variables

## What is a variable?

A variable is a named box that stores a value. You give it a name, put a
value in it with `=`, and use the name later instead of the value.

```python
name = "Hassan"
age = 20
print(name)   # Hassan
print(age)    # 20
```

The `=` sign is called **assignment**. It puts the value on the right into
the variable on the left. It does NOT mean "equal to" like in maths.

## Creating and using variables

```python
city = "Lahore"
price = 150
print(city)              # Lahore
print("Price:", price)   # Price: 150
```

You can use a variable in a calculation or inside a sentence:

```python
apples = 5
oranges = 3
total = apples + oranges
print(total)                          # 8
print(f"I have {total} fruits.")      # I have 8 fruits.
```

## Naming rules

A variable name:

1. Can contain letters (`a-z`, `A-Z`), digits (`0-9`), and underscore (`_`)
2. Cannot start with a digit
3. Cannot contain spaces or symbols like `-`, `+`, `@`
4. Cannot be a Python keyword (`if`, `for`, `class`, `True`, ...)
5. Is case-sensitive: `Age`, `age`, and `AGE` are three different variables

```python
# Good names
user_name = "Hassan"
age2 = 20
_private = 1

# Bad names — these give an error
# 2age = 20        # cannot start with a digit
# my name = "Ali"  # no spaces allowed
# class = "A"      # 'class' is a keyword
```

Good names describe the value: `user_name` is better than `x`.

## Multiple assignment

You can assign several variables on one line:

```python
x, y, z = 1, 2, 3
print(x, y, z)   # 1 2 3

a = b = c = 0
print(a, b, c)   # 0 0 0
```

## Swapping values

Swap two variables in one line — no temporary variable needed:

```python
a = 5
b = 10
a, b = b, a
print(a, b)   # 10 5
```

## Reassigning a variable

A variable can be given a new value at any time. The old value is forgotten.

```python
score = 10
print(score)   # 10
score = 25
print(score)   # 25
score = score + 5
print(score)   # 30
```

## Dynamic typing

In Python you do not declare a type. A variable can hold a number now and
a string later — Python works out the type from the value.

```python
data = 100
print(type(data))   # <class 'int'>

data = "hello"
print(type(data))   # <class 'str'>
```

`type()` tells you the type of a value. (Data types are covered in full in
Lesson 02.)

## Constants

A constant is a value that should not change. Python has no real constants,
so by convention we write constant names in `UPPER_CASE`:

```python
PI = 3.14159
MAX_USERS = 100
print(PI)         # 3.14159
```

`UPPER_CASE` is a signal to other programmers: "do not change this".

## Variables in print() and f-strings

```python
name = "Hassan"
age = 20
print("My name is", name, "and I am", age, "years old.")
print(f"My name is {name} and I am {age} years old.")
# Both print: My name is Hassan and I am 20 years old.
```

An f-string starts with `f` before the quotes. Anything inside `{ }` is
replaced by its value.

## Getting input from the user

`input()` asks the user to type something. It always returns a string.

```python
name = input("Enter your username: ")
print(f"Hello, {name}!")
```

> Note: `input()` waits for you to type. That is why the runnable file
> `variables.py` does not use `input()` — so it can run without stopping.
> Hassan's `login.py` at the repo root shows a real `input()` example.

## Common mistakes

| Mistake | Why it fails |
|---|---|
| `2age = 20` | A name cannot start with a digit |
| `my name = "Ali"` | No spaces in a name |
| `print(age)` before `age = 20` | The variable does not exist yet (`NameError`) |
| `Age` vs `age` | Different variables — case matters |
| `name = Hassan` (no quotes) | Python thinks `Hassan` is another variable |

## Run it

```bash
python3 variables.py
python3 exercises.py
python3 solutions.py
```

Next: [02 — Data Types](../02-data-types/README.md)
