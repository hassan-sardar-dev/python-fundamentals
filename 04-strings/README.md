# 04 — Strings

## What is a string?

A string (`str`) is text — letters, digits, spaces, and symbols wrapped in
quotes. Strings are one of the most used types in Python.

```python
name = "Hassan"
print(name)         # Hassan
print(type(name))   # <class 'str'>
```

## Single, double, and triple quotes

All three make strings. Pick the one that is easiest to read:

```python
single = 'hello'
double = "hello"
triple = """hello"""

# Use double quotes if the text contains an apostrophe:
sentence = "It's a nice day"   # easier than 'It\'s a nice day'

# Triple quotes make a string over several lines:
message = """Hello,
this is line two,
and this is line three."""
print(message)
```

## Indexing — getting one character

Each character has a position (index). Counting starts at **0** from the
left, and at **-1** from the right.

```python
word = "Python"
#  P  y  t  h  o  n
#  0  1  2  3  4  5
# -6 -5 -4 -3 -2 -1

print(word[0])    # P — first character
print(word[1])    # y
print(word[-1])   # n — last character
print(word[-2])   # o
# print(word[6])  # IndexError — there is no index 6
```

## Slicing — getting part of a string

Slicing uses `[start:end:step]`. It takes characters from `start` up to
(but **not including**) `end`:

```python
line = "This is a sample line of text"
print(line[0])      # T
print(line[5:10])   # "is a " — indexes 5, 6, 7, 8, 9
print(line[-5:])    # " text" — from 5th from the end to the end
print(line[:4])     # "This" — from the start to index 4
print(line[5:])     # "is a sample line of text" — from index 5 to the end
print(line[:])      # the whole string (a copy)
print(line[::2])    # "Ti sasml ieo et" — every 2nd character
print(line[::-1])   # "txet fo enil elpmas a si sihT" — reversed!
```

Leave out `start` to start at the beginning, leave out `end` to go to
the end, and use a negative step to go backwards.

## Concatenation and repetition

```python
first = "Hassan"
last = "Sardar"
print(first + " " + last)   # Hassan Sardar — + joins strings
print("Ha" * 3)             # HaHaHa — * repeats a string
print("-" * 20)             # --------------------
```

You cannot add a string and a number — convert the number first:

```python
age = 20
# print("Age: " + age)        # TypeError
print("Age: " + str(age))     # Age: 20 — correct
print(f"Age: {age}")          # Age: 20 — f-strings do this for you
```

## `len()`, `in`, and `not in`

```python
name = "Hassan"
print(len(name))          # 6 — number of characters

print("H" in name)        # True
print("z" in name)        # False
print("z" not in name)    # True
print("ass" in name)      # True — checks a part of the string too
```

## f-strings

An f-string starts with `f` before the quotes. Anything inside `{ }` is
replaced by its value, and you can even do maths inside:

```python
name = "Hassan"
age = 20
print(f"My name is {name} and I am {age} years old.")
print(f"Next year I will be {age + 1}.")
print(f"My name in upper case is {name.upper()}.")
```

## Escape characters

Some characters are hard to type directly. A backslash `\` escapes them:

| Escape | Meaning | Example |
|---|---|---|
| `\n` | New line | `"Hello\nWorld"` |
| `\t` | Tab | `"Name:\tHassan"` |
| `\\` | A backslash | `"C:\\Users\\Hassan"` |
| `\"` | A double quote inside double quotes | `"He said \"Hi\""` |
| `\'` | A single quote inside single quotes | `'It\'s fine'` |

```python
print("Hello\nWorld")   # Hello (new line) World
print("Name:\tHassan")  # Name:    Hassan
```

## Immutability — strings cannot be changed in place

```python
name = "Hassan"
# name[0] = "h"   # TypeError — strings are immutable
name = "hassan"   # this is fine: it makes a NEW string
print(name)       # hassan
```

Every string method below returns a **new** string. The original does not
change unless you save the result:

```python
word = "hello"
print(word.upper())  # HELLO
print(word)          # hello — unchanged!
word = word.upper()
print(word)          # HELLO — now it changed, because we saved the result
```

## String methods — complete table

Here is every common string method, with a one-line example each.
`text` in the examples is `"  Hello, Hassan!  "` unless stated otherwise.

### Changing case

| Method | What it does | Example |
|---|---|---|
| `upper()` | ALL CAPITALS | `"hello".upper()` → `"HELLO"` |
| `lower()` | all lower case | `"Hello".lower()` → `"hello"` |
| `title()` | First Letter Of Each Word | `"my name is hassan".title()` → `"My Name Is Hassan"` |
| `capitalize()` | First letter upper, rest lower | `"hello world".capitalize()` → `"Hello world"` |
| `casefold()` | Lower case, stronger than `lower()` (best for comparing) | `"HELLO".casefold()` → `"hello"` |

### Removing spaces

| Method | What it does | Example |
|---|---|---|
| `strip()` | Removes spaces from both ends | `"  hi  ".strip()` → `"hi"` |
| `lstrip()` | Removes spaces from the left | `"  hi  ".lstrip()` → `"hi  "` |
| `rstrip()` | Removes spaces from the right | `"  hi  ".rstrip()` → `"  hi"` |

### Splitting and joining

| Method | What it does | Example |
|---|---|---|
| `split()` | Splits into a list (on spaces by default) | `"a b c".split()` → `['a', 'b', 'c']` |
| `rsplit()` | Splits from the right | `"a,b,c".rsplit(",", 1)` → `['a,b', 'c']` |
| `join()` | Joins a list into one string | `"-".join(["a", "b"])` → `"a-b"` |

### Searching and replacing

| Method | What it does | Example |
|---|---|---|
| `replace(old, new)` | Replaces text | `"hello".replace("l", "L")` → `"heLLo"` |
| `find(sub)` | Index of `sub`, or `-1` if not found | `"hello".find("l")` → `2` |
| `index(sub)` | Index of `sub`, or an error if not found | `"hello".index("l")` → `2` |
| `count(sub)` | How many times `sub` appears | `"hello".count("l")` → `2` |
| `startswith(prefix)` | `True` if the string starts with it | `"hello".startswith("he")` → `True` |
| `endswith(suffix)` | `True` if the string ends with it | `"hello".endswith("lo")` → `True` |

### Checking the contents — these return `True` or `False`

| Method | What it does | Example |
|---|---|---|
| `isalpha()` | Only letters? | `"abc".isalpha()` → `True`, `"ab1".isalpha()` → `False` |
| `isdigit()` | Only digits? | `"123".isdigit()` → `True`, `"12a".isdigit()` → `False` |
| `isalnum()` | Only letters and digits? | `"abc123".isalnum()` → `True`, `"ab c".isalnum()` → `False` |
| `isspace()` | Only spaces? | `"   ".isspace()` → `True`, `" a ".isspace()` → `False` |

## Hassan's first string examples — fixed and expanded

Hassan's original `string.py` used these methods. Here they are, corrected
and with more added:

```python
name = 'my name is hassan'
print(name)                 # my name is hassan
print(name.upper())         # MY NAME IS HASSAN
print(name.lower())         # my name is hassan
print(name.title())         # My Name Is Hassan — first letter of each word
print(name.capitalize())    # My name is hassan — first letter of the string
print(name.split(" "))      # ['my', 'name', 'is', 'hassan']

age = 20
print(f'My name is {name} and I am {age} years old')

line = "This is a sample line of text"
print(line[0])              # T
print(line[5:10])           # is a
print(line[-5:])            #  text
print(line.replace("sample", "test"))  # This is a test line of text
print(line.find("line"))    # 10 — index where "line" starts
print(line.count("is"))     # 2 — "is" appears in "This" and "is"
```

## Hassan's username check, as a string example

From `main.py` / `login.py` — a function that checks a name using a
string comparison:

```python
def username(name):
    if name == "Hassan":
        return "This is valid username"
    else:
        return "This is not a valid username"

print(username("Hassan"))  # This is valid username
print(username("Ali"))     # This is not a valid username
```

A stricter version, using string methods so `"  hassan  "` also works:

```python
def check_username(name):
    return name.strip().title() == "Hassan"

print(check_username("  hassan  "))  # True
print(check_username("Ali"))         # False
```

## Common mistakes

| Mistake | What happens |
|---|---|
| `name[0] = "h"` | `TypeError` — strings are immutable |
| `"Age: " + 20` | `TypeError` — use `str(20)` or an f-string |
| Forgetting `upper()` returns a new string | The original is unchanged until you save it |
| `find()` vs `index()` | `find()` returns `-1` when not found; `index()` raises an error |
| `word[6]` on a 6-letter word | `IndexError` — indexes go from `0` to `len - 1` |

## Run it

```bash
python3 strings.py
python3 exercises.py
python3 solutions.py
```

Next: Conditionals and Loops (coming next)
