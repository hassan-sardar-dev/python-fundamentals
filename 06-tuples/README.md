# 06 — Tuples

## What is a tuple?

A tuple (`tuple`) is a collection of items in one variable. It is:

- **Ordered** — items stay in the order you put them in
- **Immutable** — you cannot change, add, or remove items after creating it
- **Allows duplicates** — the same value can appear more than once

Use round brackets `( )` and separate items with commas:

```python
point = (10, 20)
print(point)         # (10, 20)
print(type(point))   # <class 'tuple'>
print(len(point))    # 2 — number of items

colours = ("red", "green", "blue", "red")
print(colours)       # ('red', 'green', 'blue', 'red')
```

A tuple can hold different types together:

```python
student = ("Hassan", 20, 85.5)
print(student)   # ('Hassan', 20, 85.5)
```

## Creating tuples — the tricky cases

```python
empty = ()                 # an empty tuple
print(empty)               # ()

numbers = tuple([1, 2, 3])  # tuple() turns a list into a tuple
print(numbers)             # (1, 2, 3)

# A single-item tuple NEEDS a trailing comma:
one = (5,)
print(one)                 # (5,)
print(type(one))           # <class 'tuple'>

# Without the comma, it is NOT a tuple — just a number in brackets:
not_a_tuple = (5)
print(not_a_tuple)         # 5
print(type(not_a_tuple))   # <class 'int'>
```

That trailing comma is the most common tuple mistake. `(5,)` is a tuple;
`(5)` is just the number `5`.

You can also make a tuple without brackets — the commas make the tuple:

```python
point = 10, 20
print(point)         # (10, 20)
print(type(point))   # <class 'tuple'>
```

## Indexing — getting one item

Counting starts at **0** from the left, and at **-1** from the right —
exactly like lists and strings:

```python
colours = ("red", "green", "blue")
#  red       green      blue
#  0         1          2
# -3        -2         -1

print(colours[0])    # red — first item
print(colours[1])    # green
print(colours[-1])   # blue — last item
print(colours[-2])   # green
# print(colours[3])  # IndexError — there is no index 3
```

## Slicing — getting part of a tuple

Slicing uses `[start:end:step]` and returns a **new** tuple:

```python
numbers = (10, 20, 30, 40, 50, 60)
print(numbers[1:4])   # (20, 30, 40) — indexes 1, 2, 3
print(numbers[:3])    # (10, 20, 30) — from the start to index 3
print(numbers[3:])    # (40, 50, 60) — from index 3 to the end
print(numbers[:])     # (10, 20, 30, 40, 50, 60) — a copy of the whole tuple
print(numbers[::2])   # (10, 30, 50) — every 2nd item
print(numbers[::-1])  # (60, 50, 40, 30, 20, 10) — reversed!
```

## `len()`, `in`, and `not in`

```python
colours = ("red", "green", "blue")
print(len(colours))           # 3 — number of items

print("green" in colours)       # True
print("yellow" in colours)      # False
print("yellow" not in colours)  # True
```

## Immutability — you cannot change a tuple

This is the whole point of a tuple. Once it is made, it stays the same:

```python
point = (10, 20)
# point[0] = 30   # TypeError — tuples are immutable
# point.append(30)  # AttributeError — tuples have no append()
# del point[0]      # TypeError — you cannot delete an item
```

If you need to "change" a tuple, make a new one instead:

```python
point = (10, 20)
point = (30, 20)   # fine — this makes a NEW tuple and reuses the name
print(point)       # (30, 20)
```

> Note: a tuple can hold a mutable item, like a list, and that list can
> still change — but the tuple itself never gains or loses items:
>
> ```python
> data = (1, [2, 3])
> data[1].append(4)
> print(data)   # (1, [2, 3, 4]) — the list inside changed, the tuple did not
> ```

## Unpacking — giving each item a name

Unpacking takes the items out of a tuple and puts each one into its own
variable. The number of variables must match the number of items:

```python
student = ("Hassan", 20, 85)
name, age, marks = student
print(name)    # Hassan
print(age)     # 20
print(marks)   # 85
```

This is the easy way to swap two variables (you saw this in Lesson 01 —
it works because `(b, a)` is a tuple):

```python
a = 5
b = 10
a, b = b, a
print(a, b)   # 10 5
```

You can also unpack with a star `*` to collect the rest into a list:

```python
numbers = (1, 2, 3, 4, 5)
first, second, *rest = numbers
print(first)    # 1
print(second)   # 2
print(rest)     # [3, 4, 5] — the rest, as a list
```

## Tuple methods — only two!

A tuple has only **two** methods. That is because it is immutable — there
is nothing to add, remove, or sort, so it does not need those methods.

| Method | What it does | Example |
|---|---|---|
| `count(value)` | How many times a value appears | `colours.count("red")` → `2` |
| `index(value)` | Index of the **first** matching item | `colours.index("green")` → `1` |

```python
colours = ("red", "green", "blue", "red")
print(colours.count("red"))    # 2
print(colours.count("yellow")) # 0
print(colours.index("green"))  # 1
print(colours.index("red"))    # 0 — the FIRST "red"
# colours.index("yellow")  # ValueError — "yellow" is not in the tuple
```

## Tuple vs list — which one to use?

|  | List `[]` | Tuple `()` |
|---|---|---|
| Ordered? | Yes | Yes |
| Allows duplicates? | Yes | Yes |
| Can change items? | Yes — mutable | No — immutable |
| Methods | Many (`append`, `remove`, `sort`, ...) | Only 2 (`count`, `index`) |
| Speed | A little slower | A little faster |
| Use when... | The data will change | The data should stay fixed |

Use a **list** when the data will grow or change — a shopping list, marks
that get new results. Use a **tuple** when the data is fixed and should not
change by mistake — coordinates, a date `(2026, 11, 15)`, a student record.

```python
# A shopping list changes — use a list:
shopping = ["milk", "bread"]
shopping.append("eggs")

# A point on a map is fixed — use a tuple:
point = (10, 20)
```

## Nested tuples — a tuple inside a tuple

```python
students = (("Hassan", 85), ("Ali", 90), ("Sara", 78))
print(students[0])        # ('Hassan', 85) — the first student
print(students[0][0])     # Hassan
print(students[1][1])     # 90 — marks of the second student

# Unpacking inside a loop (loops are covered in full in Lesson 07):
for name, marks in students:
    print(name, marks)
# Hassan 85
# Ali 90
# Sara 78
```

## Returning multiple values from a function

A function can return a tuple, so it can give back more than one value at
once. Functions are covered in full in Lesson 08 — for now, just see the
pattern:

```python
def get_student():
    return ("Hassan", 20, 85)

name, age, marks = get_student()
print(name)    # Hassan
print(age)     # 20
print(marks)   # 85
```

## Converting between lists and tuples

```python
fruits_list = ["apple", "banana", "mango"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)   # ('apple', 'banana', 'mango')

names_tuple = ("Hassan", "Ali", "Sara")
names_list = list(names_tuple)
print(names_list)     # ['Hassan', 'Ali', 'Sara']
names_list.append("Zain")   # now it can change — it is a list again
print(names_list)     # ['Hassan', 'Ali', 'Sara', 'Zain']
```

A handy trick: to "change" a tuple, convert it to a list, change the list,
and convert it back.

## A practical example — a student record

```python
student = ("Hassan", 20, 85)
name, age, marks = student
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Marks: {marks}")

# Coordinates — a point that should not move by mistake:
point = (10, 20)
x, y = point
print(f"Point is at x={x}, y={y}")
```

And a small class record — a tuple of tuples:

```python
class_marks = (("Hassan", 85), ("Ali", 90), ("Sara", 78))
print("Students:", len(class_marks))   # 3
print("Top student:", class_marks[1])  # ('Ali', 90)
```

## Common mistakes

| Mistake | What happens |
|---|---|
| `(5)` instead of `(5,)` | You made an `int`, not a tuple |
| `point[0] = 30` | `TypeError` — tuples are immutable |
| `point.append(30)` | `AttributeError` — tuples have no `append()` |
| `name, age = ("Hassan", 20, 85)` | `ValueError` — 3 items, but only 2 variables |
| `colours.index("yellow")` when it is not there | `ValueError` — check with `in` first |
| Using a list where a tuple would be safer | The data can be changed by mistake later |

## Run it

```bash
python3 tuples.py
python3 exercises.py
python3 solutions.py
```

Next: Conditionals and Loops (coming next)
