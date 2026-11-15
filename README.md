# Python Fundamentals

A beginner-friendly Python tutorial, built step by step with simple English,
lots of runnable examples, exercises, and solutions.

This is Hassan Sardar's Python learning series. It starts from zero and
builds up to real programs and projects.

## How to use this repo

Each lesson lives in its own folder. Every folder has:

- `README.md` — the lesson: explanations + examples + expected output
- `<topic>.py` — runnable code for the lesson (run it and see the output)
- `exercises.py` — 5 exercises to try yourself (no answers inside)
- `solutions.py` — full solutions for those 5 exercises

Run a lesson like this:

```bash
python3 01-variables/variables.py
python3 02-data-types/data_types.py
python3 03-numbers/numbers.py
python3 04-strings/strings.py
```

Run the exercises the same way, then check your work against the solutions:

```bash
python3 01-variables/exercises.py
python3 01-variables/solutions.py
```

You only need Python 3 installed. No extra packages are needed — every
file uses only the Python standard library.

## Table of contents

| # | Lesson | Folder | Status |
|---|--------|--------|--------|
| 01 | Variables | [01-variables](01-variables/README.md) | ✅ Done |
| 02 | Data Types | [02-data-types](02-data-types/README.md) | ✅ Done |
| 03 | Numbers | [03-numbers](03-numbers/README.md) | ✅ Done |
| 04 | Strings | [04-strings](04-strings/README.md) | ✅ Done |
| 05 | Conditionals and Loops | — | Coming next |
| 06 | Functions and Modules | — | Coming next |
| 07 | Collections (Lists, Tuples, Sets, Dictionaries) | — | Coming next |
| 08 | File Handling and Exceptions | — | Coming next |
| 09 | Object-Oriented Programming | — | Coming next |
| 10 | Advanced Python and Projects | — | Coming next |

## Full learning path

1. ✅ **Variables** — what a variable is, naming rules, assignment
2. ✅ **Data Types** — int, float, str, bool, None, list, tuple, set, dict
3. ✅ **Numbers** — arithmetic, `math`, `random`, formatting
4. ✅ **Strings** — indexing, slicing, f-strings, and every common method
5. **Conditionals and Loops** — `if` / `elif` / `else`, `for`, `while`
6. **Functions and Modules** — `def`, arguments, return values, imports
7. **Collections** — lists, tuples, sets, and dictionaries in depth
8. **File Handling and Exceptions** — reading/writing files, `try` / `except`
9. **Object-Oriented Programming** — classes, objects, inheritance
10. **Advanced Python and Projects** — putting it all together

## Hassan's first examples

The original files at the root of the repo are Hassan's very first Python
examples, and they still work:

- `main.py` — `username()` returns "This is valid username" only for `"Hassan"`
- `login.py` — asks for a username with `input()` and checks it with `username()`
- `number.py` — first number examples (`math`, `round`, `floor`, `ceil`, ...)
- `string.py` — first string examples (`upper`, `lower`, `title`, `split`, ...)

Run them with:

```bash
python3 login.py     # enter Hassan to see the valid username message
python3 number.py
python3 string.py
```

Lessons 03 and 04 take those first number and string examples, fix the
small mistakes in them, and expand them into complete tutorials.

## Goal

Build a strong understanding of Python fundamentals, then gradually apply
that knowledge to more advanced programs and real-world projects.
