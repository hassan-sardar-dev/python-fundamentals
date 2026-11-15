"""Task 2 — Copy or not? (Lists: aliasing vs copying).

Make b = a and c = a.copy(). Change a.
Explain what b and c show.

Run it with:
    python3 copy_or_not.py
"""

a = [1, 2, 3]
print("Start:  a =", a)

# b = a does NOT make a new list.
# b is just another name for the SAME list as a.
b = a

# c = a.copy() DOES make a new list.
# c has the same items as a, but it is a separate list.
c = a.copy()

print("b = a       -> b =", b)
print("c = a.copy() -> c =", c)
print("a is b:", a is b)   # True  — same list in memory
print("a is c:", a is c)   # False — different list in memory

# Now change a
a.append(4)
a[0] = 10
print()
print("After changing a (append 4, set a[0] = 10):")
print("a =", a)
print("b =", b)
print("c =", c)

print()
print("Explanation:")
print("b changed too, because b = a means b IS a —")
print("both names point to the same list, so a change")
print("through one name shows up through the other.")
print("c did NOT change, because c = a.copy() made a")
print("separate list. Changing a leaves c alone.")
print("Rule: use .copy() (or list(a) / a[:]) when you")
print("want a real copy that will not change with the original.")
