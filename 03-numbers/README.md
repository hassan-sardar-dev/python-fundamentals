# 03 — Numbers

## int, float, and complex

Python has three number types:

```python
a = 10          # int — whole number
b = 3.5         # float — number with a decimal point
c = 2 + 3j      # complex — real + imaginary part (rarely used by beginners)

print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'complex'>
```

If you mix an `int` and a `float`, the result is a `float`:

```python
print(10 + 3.5)   # 13.5
print(type(10 + 3.5))  # <class 'float'>
```

## Arithmetic operators

| Operator | Name | Example | Result |
|---|---|---|---|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `5 / 2` | `2.5` |
| `//` | Floor division | `5 // 2` | `2` |
| `%` | Remainder (modulo) | `5 % 2` | `1` |
| `**` | Power | `2 ** 3` | `8` |

```python
print(5 + 3)    # 8
print(5 - 3)    # 2
print(5 * 3)    # 15
print(5 / 2)    # 2.5  — normal division always gives a float
print(5 // 2)   # 2    — floor division drops the decimal part
print(5 % 2)    # 1    — remainder: 5 = 2 * 2 + 1
print(2 ** 3)   # 8    — 2 * 2 * 2
print(10 % 3)   # 1
print(-7 // 2)  # -4   — floor division rounds DOWN, not towards zero
```

`%` is very useful: `number % 2 == 0` means the number is even.

## Precedence — which operation runs first?

Python follows the same order as maths (BODMAS / PEMDAS):

1. Brackets `( )`
2. Power `**`
3. Multiplication `*`, division `/`, `//`, `%` (left to right)
4. Addition `+`, subtraction `-` (left to right)

```python
print(2 + 3 * 4)      # 14, not 20 — * runs before +
print((2 + 3) * 4)    # 20 — brackets run first
print(2 ** 3 ** 2)    # 512 — ** runs right to left: 2 ** (3 ** 2) = 2 ** 9
print(10 - 4 - 3)     # 3 — left to right: (10 - 4) - 3
```

When in doubt, add brackets. They make your code clear.

## Built-in number functions

These are built into Python — no import needed:

```python
print(round(10.5))   # 10 — rounds to the nearest even number on .5
print(round(10.6))   # 11
print(round(3.14159, 2))  # 3.14 — round to 2 decimal places
print(abs(-7))       # 7 — absolute value (distance from zero)
print(min(3, 1, 9))  # 1
print(max(3, 1, 9))  # 9
print(pow(2, 3))     # 8 — same as 2 ** 3
print(sum([1, 2, 3, 4]))  # 10
```

> Note: `round(10.5)` gives `10`, not `11`. Python uses "banker's
> rounding": a `.5` rounds to the nearest *even* number. `round(11.5)` is
> `12`. For money, round to 2 decimals instead: `round(2.675, 2)`.

## The `math` module

For more maths, import the `math` module:

```python
import math

print(math.floor(12.3))   # 12 — rounds DOWN to the nearest whole number
print(math.ceil(12.3))    # 13 — rounds UP to the nearest whole number
print(math.sqrt(16))      # 4.0 — square root
print(math.pow(2, 3))     # 8.0 — power (returns a float, unlike **)
print(math.log(10))       # 2.302... — natural logarithm (base e)
print(math.log10(100))    # 2.0 — logarithm base 10
print(math.sin(0))        # 0.0
print(math.cos(0))        # 1.0
print(math.pi)            # 3.141592653589793
print(math.e)             # 2.718281828459045
```

`floor` and `ceil` are different from `round`: `floor` always goes down,
`ceil` always goes up, `round` goes to the nearest.

Hassan's first `number.py` used these same methods — here they are fixed
and expanded (the comment there said "mehtods", which is now "methods"):

```python
import math
num = 100
print(type(num))       # <class 'int'>
print(num + 1999)      # 2099
print(round(10.5))     # 10
print(math.floor(12.3))  # 12
print(math.ceil(12.3))   # 13
print(abs(12.3))         # 12.3
print(pow(12.3, 2))      # 151.29
print(math.sqrt(12.3))   # 3.507...
print(math.log(12.3))    # 2.509...
```

## The `random` module

```python
import random

data = [1, 2, 3, 4, 5]
print(random.choice(data))    # one random item from the list

print(random.randint(1, 10))  # a random integer from 1 to 10 (both included)
print(random.randrange(0, 10, 2))  # 0, 2, 4, 6 or 8 — like range()
print(random.random())        # a random float from 0.0 up to (not including) 1.0
print(random.uniform(1, 5))   # a random float between 1 and 5
```

Use `random.seed(42)` if you want the same "random" numbers every time —
useful for testing.

## Formatting numbers

```python
price = 49.99
print(f"Price: {price}")            # Price: 49.99
print(f"Price: {price:.2f}")        # Price: 49.99 — always 2 decimal places
print(f"Price: {price:.0f}")        # Price: 50 — no decimal places
print(f"Big number: {1000000:,}")   # Big number: 1,000,000 — commas
print(f"Percent: {0.856:.1%}")      # Percent: 85.6%
print(f"Pi: {3.14159:.3f}")         # Pi: 3.142
```

## Common mistakes

### `/` vs `//`

```python
print(7 / 2)    # 3.5 — normal division, always a float
print(7 // 2)   # 3   — floor division, drops the decimal part
```

### Float precision: `0.1 + 0.2`

Computers store decimals in binary, so some decimals are not exact:

```python
print(0.1 + 0.2)   # 0.30000000000000004 — not exactly 0.3!
print(0.1 + 0.2 == 0.3)   # False
```

Fix it by rounding, or by comparing with a small tolerance:

```python
print(round(0.1 + 0.2, 2))              # 0.3
print(abs((0.1 + 0.2) - 0.3) < 0.0001)  # True
```

For money, use `round(..., 2)` or the `decimal` module — never trust
raw float equality.

### Dividing by zero

```python
# print(10 / 0)   # ZeroDivisionError — division by zero is not allowed
```

### `int()` cuts off decimals — it does not round

```python
print(int(3.9))    # 3 — not 4
print(round(3.9))  # 4
```

## Run it

```bash
python3 numbers.py
python3 exercises.py
python3 solutions.py
```

Next: [04 — Strings](../04-strings/README.md)
