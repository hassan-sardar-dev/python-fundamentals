# Practise — 15 November 2026

Four hands-on tasks, 30 minutes. Lists and tuples, from Lessons 05 and 06.

## The tasks

| # | Task | File | What it practises |
|---|------|------|-------------------|
| 1 | Shopping cart | [shopping_cart.py](shopping_cart.py) | `append`, `insert`, `pop`, `remove` — print after each step |
| 2 | Copy or not? | [copy_or_not.py](copy_or_not.py) | `b = a` vs `c = a.copy()` — aliasing vs a real copy |
| 3 | Table of 7 | [table_of_7.py](table_of_7.py) | List comprehension — `[7, 14, ..., 70]` |
| 4 | Student record | [student_record.py](student_record.py) | Tuple, unpacking, f-string |

## Run them

```bash
python3 shopping_cart.py
python3 copy_or_not.py
python3 table_of_7.py
python3 student_record.py
```

No extra packages needed — only the Python standard library, and no `input()`, so every file runs start to finish.

## Expected output

**1. Shopping cart**

```
Start: ['milk', 'bread']
After append('eggs'): ['milk', 'bread', 'eggs']
After insert(1, 'cheese'): ['milk', 'cheese', 'bread', 'eggs']
Popped item: eggs
After pop(): ['milk', 'cheese', 'bread']
After remove('bread'): ['milk', 'cheese']
Final cart: ['milk', 'cheese']
```

**2. Copy or not?**

```
Start:  a = [1, 2, 3]
b = a       -> b = [1, 2, 3]
c = a.copy() -> c = [1, 2, 3]
a is b: True
a is c: False

After changing a (append 4, set a[0] = 10):
a = [10, 2, 3, 4]
b = [10, 2, 3, 4]
c = [1, 2, 3]
```

The lesson: `b = a` does **not** copy — `b` is the same list, so it changes with `a`. `c = a.copy()` **does** copy — `c` is a separate list, so it stays as it was.

**3. Table of 7**

```
Table of 7: [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
Same with a loop: [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
Both are equal: True
```

**4. Student record**

```
Student tuple: (101, 'Hassan', 85)
Roll No: 101, Name: Hassan, Marks: 85
Roll No: 102, Name: Ali, Marks: 92
```
