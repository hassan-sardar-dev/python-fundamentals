# 05 — Lists

## What is a list?

A list (`list`) is a collection of items in one variable. It is:

- **Ordered** — items stay in the order you put them in
- **Mutable** — you can change, add, and remove items after creating it
- **Allows duplicates** — the same value can appear more than once

Use square brackets `[ ]` and separate items with commas:

```python
fruits = ["apple", "banana", "mango", "apple"]
print(fruits)         # ['apple', 'banana', 'mango', 'apple']
print(type(fruits))   # <class 'list'>
print(len(fruits))    # 4 — number of items
```

A list can hold different types together, but it is usually best to keep
one kind of thing in one list:

```python
numbers = [1, 2, 3, 4, 5]
mixed = ["Hassan", 20, True]   # works, but harder to read
empty = []                     # an empty list
print(empty)                   # []
```

Lists are the most used collection in Python. You met them briefly in
Lesson 02 — now we go through them properly.

## Indexing — getting one item

Counting starts at **0** from the left, and at **-1** from the right —
exactly like strings (Lesson 04):

```python
fruits = ["apple", "banana", "mango", "orange"]
#  apple     banana     mango      orange
#  0         1          2          3
# -4        -3         -2         -1

print(fruits[0])    # apple — first item
print(fruits[1])    # banana
print(fruits[-1])   # orange — last item
print(fruits[-2])   # mango
# print(fruits[4])  # IndexError — there is no index 4
```

## Slicing — getting part of a list

Slicing uses `[start:end:step]`. It takes items from `start` up to (but
**not including**) `end`, and returns a **new** list:

```python
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[1:4])   # [20, 30, 40] — indexes 1, 2, 3
print(numbers[:3])    # [10, 20, 30] — from the start to index 3
print(numbers[3:])    # [40, 50, 60] — from index 3 to the end
print(numbers[:])     # [10, 20, 30, 40, 50, 60] — a copy of the whole list
print(numbers[::2])   # [10, 30, 50] — every 2nd item
print(numbers[::-1])  # [60, 50, 40, 30, 20, 10] — reversed!
```

## `len()`, `in`, and `not in`

```python
fruits = ["apple", "banana", "mango"]
print(len(fruits))           # 3 — number of items

print("banana" in fruits)       # True
print("grapes" in fruits)       # False
print("grapes" not in fruits)   # True
```

## Changing items

Lists are mutable, so you can change an item by its index:

```python
fruits = ["apple", "banana", "mango"]
fruits[1] = "grapes"     # replace the item at index 1
print(fruits)            # ['apple', 'grapes', 'mango']

fruits[0:2] = ["kiwi", "pear"]   # replace a slice with new items
print(fruits)            # ['kiwi', 'pear', 'mango']
```

## Adding items — `append()`, `extend()`, `insert()`

| Method | What it does | Example |
|---|---|---|
| `append(item)` | Adds one item to the **end** | `fruits.append("mango")` |
| `extend(list)` | Adds **all items** from another list to the end | `fruits.extend(["kiwi", "pear"])` |
| `insert(index, item)` | Adds one item at a position | `fruits.insert(1, "banana")` |

```python
fruits = ["apple", "banana"]
fruits.append("mango")
print(fruits)   # ['apple', 'banana', 'mango']

fruits.extend(["kiwi", "pear"])
print(fruits)   # ['apple', 'banana', 'mango', 'kiwi', 'pear']

fruits.insert(1, "grapes")
print(fruits)   # ['apple', 'grapes', 'banana', 'mango', 'kiwi', 'pear']
```

`append()` adds one item; `extend()` adds many. A common beginner mistake
is using `append()` with a list — it adds the whole list as **one** item:

```python
fruits = ["apple"]
fruits.append(["banana", "mango"])
print(fruits)   # ['apple', ['banana', 'mango']] — a list inside a list!
```

## Removing items — `remove()`, `pop()`, `clear()`, `del`

| Method | What it does | Example |
|---|---|---|
| `remove(value)` | Removes the **first** item with that value | `fruits.remove("banana")` |
| `pop(index)` | Removes the item at an index and **returns** it | `fruits.pop(1)` |
| `pop()` | Removes the **last** item and returns it | `fruits.pop()` |
| `clear()` | Removes **all** items | `fruits.clear()` |
| `del list[index]` | Removes the item at an index (no return value) | `del fruits[0]` |

```python
fruits = ["apple", "banana", "mango", "banana"]
fruits.remove("banana")   # removes only the FIRST "banana"
print(fruits)             # ['apple', 'mango', 'banana']

last = fruits.pop()       # removes the last item and gives it back
print(last)               # banana
print(fruits)             # ['apple', 'mango']

first = fruits.pop(0)     # removes the item at index 0
print(first)              # apple
print(fruits)             # ['mango']

del fruits[0]             # removes the item at index 0
print(fruits)             # []

fruits = ["apple", "banana"]
fruits.clear()            # empties the whole list
print(fruits)             # []
```

`remove("banana")` gives an error (`ValueError`) if `"banana"` is not in
the list — check with `in` first if you are not sure.

## Finding items — `index()` and `count()`

| Method | What it does | Example |
|---|---|---|
| `index(value)` | Index of the **first** matching item | `fruits.index("mango")` → `2` |
| `count(value)` | How many times a value appears | `fruits.count("apple")` → `2` |

```python
fruits = ["apple", "banana", "mango", "apple"]
print(fruits.index("mango"))   # 2
print(fruits.index("apple"))   # 0 — the FIRST "apple"
print(fruits.count("apple"))   # 2
print(fruits.count("kiwi"))    # 0
# fruits.index("kiwi")   # ValueError — "kiwi" is not in the list
```

## Sorting and reversing — `sort()` and `reverse()`

| Method | What it does | Example |
|---|---|---|
| `sort()` | Sorts the list **in place** (changes the original) | `numbers.sort()` |
| `sort(reverse=True)` | Sorts largest first | `numbers.sort(reverse=True)` |
| `reverse()` | Reverses the order **in place** | `numbers.reverse()` |
| `sorted(list)` | Returns a **new** sorted list, original unchanged | `sorted(numbers)` |

```python
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print(numbers)   # [1, 2, 5, 7, 9]

numbers.sort(reverse=True)
print(numbers)   # [9, 7, 5, 2, 1]

numbers.reverse()
print(numbers)   # [1, 2, 5, 7, 9] — reversed, not sorted!

names = ["Hassan", "Ali", "Sara"]
print(sorted(names))   # ['Ali', 'Hassan', 'Sara'] — a new list
print(names)           # ['Hassan', 'Ali', 'Sara'] — original unchanged
```

`sort()` changes the original list and returns `None`, so do not write
`numbers = numbers.sort()` — that would set `numbers` to `None`.

## Concatenation and repetition

```python
a = [1, 2, 3]
b = [4, 5]
print(a + b)    # [1, 2, 3, 4, 5] — + joins two lists
print(a * 3)    # [1, 2, 3, 1, 2, 3, 1, 2, 3] — * repeats a list
```

## Copying vs aliasing — a very common mistake

Assigning a list to a new variable does **not** copy it. Both names point
to the **same** list:

```python
list1 = [1, 2, 3]
list2 = list1        # alias — NOT a copy!
list2.append(4)
print(list1)         # [1, 2, 3, 4] — list1 changed too!
print(list2)         # [1, 2, 3, 4]
```

To make a real copy, use `copy()` or `list()` or a slice `[:]`:

```python
list1 = [1, 2, 3]
list2 = list1.copy()   # a real copy
list3 = list(list1)    # also a real copy
list4 = list1[:]       # also a real copy
list2.append(4)
print(list1)           # [1, 2, 3] — unchanged
print(list2)           # [1, 2, 3, 4]
```

## Nested lists — a list inside a list

```python
students = [["Hassan", 85], ["Ali", 90], ["Sara", 78]]
print(students[0])        # ['Hassan', 85] — the first student
print(students[0][0])     # Hassan — first item of the first student
print(students[1][1])     # 90 — marks of the second student
print(students[2][0])     # Sara
```

## Looping through a list (a quick preview)

A `for` loop visits each item in turn. Loops are covered in full in
Lesson 07 — for now, just read this and see the pattern:

```python
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)
# apple
# banana
# mango
```

## List comprehension — a short way to build a list

A list comprehension builds a new list in one line. It is a shortcut for
a loop that appends to a list:

```python
# The long way:
squares = []
for n in [1, 2, 3, 4, 5]:
    squares.append(n * n)
print(squares)   # [1, 4, 9, 16, 25]

# The short way — list comprehension:
squares = [n * n for n in [1, 2, 3, 4, 5]]
print(squares)   # [1, 4, 9, 16, 25]

# With a condition — only even numbers:
evens = [n for n in [1, 2, 3, 4, 5, 6] if n % 2 == 0]
print(evens)     # [2, 4, 6]

# From strings:
names = ["hassan", "ali", "sara"]
upper_names = [name.upper() for name in names]
print(upper_names)   # ['HASSAN', 'ALI', 'SARA']
```

Read it as: "give me `n * n` for each `n` in the list". You do not need
to master this yet — just recognise it when you see it.

## A practical example — student marks

```python
marks = [85, 90, 78, 92, 88]
print("Marks:", marks)
print("Total:", sum(marks))              # 433
print("Average:", sum(marks) / len(marks))  # 86.6
print("Highest:", max(marks))            # 92
print("Lowest:", min(marks))             # 78

marks.append(95)          # a new test result
marks.sort(reverse=True)  # best first
print("Sorted:", marks)   # [95, 92, 90, 88, 85, 78]
print("Top score:", marks[0])   # 95
```

And a shopping list:

```python
shopping = ["milk", "bread", "eggs"]
shopping.append("butter")
shopping.remove("bread")
print(shopping)          # ['milk', 'eggs', 'butter']
print("Items:", len(shopping))   # 3
```

## List methods — complete table

| Method | What it does |
|---|---|
| `append(item)` | Adds one item to the end |
| `extend(list)` | Adds all items from another list to the end |
| `insert(index, item)` | Adds one item at a position |
| `remove(value)` | Removes the first item with that value |
| `pop(index)` | Removes and returns the item at an index (`pop()` = last item) |
| `clear()` | Removes all items |
| `index(value)` | Index of the first matching item |
| `count(value)` | How many times a value appears |
| `sort()` | Sorts the list in place |
| `reverse()` | Reverses the order in place |
| `copy()` | Returns a copy of the list |

## Common mistakes

| Mistake | What happens |
|---|---|
| `fruits[4]` on a 4-item list | `IndexError` — indexes go from `0` to `len - 1` |
| `list2 = list1` then changing `list2` | `list1` changes too — it is an alias, not a copy |
| `numbers = numbers.sort()` | `numbers` becomes `None` — `sort()` changes the list in place |
| `fruits.append(["a", "b"])` | Adds one item (a list) — use `extend()` to add two items |
| `remove("kiwi")` when `"kiwi"` is not in the list | `ValueError` — check with `in` first |
| Changing a list while looping over it | Items get skipped — loop over a copy (`fruits[:]`) instead |

## Run it

```bash
python3 lists.py
python3 exercises.py
python3 solutions.py
```

Next: [06 — Tuples](../06-tuples/README.md)
