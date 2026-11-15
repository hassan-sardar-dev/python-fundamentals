"""Task 4 — Student record (Tuples).

Store (roll no, name, marks) as a tuple, unpack it,
print it with an f-string.

Run it with:
    python3 student_record.py
"""

# A tuple is ordered and cannot be changed — perfect for
# a fixed record like (roll no, name, marks).
student = (101, "Hassan", 85)
print("Student tuple:", student)

# Unpacking: each value goes into its own variable,
# in the same order as in the tuple.
roll_no, name, marks = student

print(f"Roll No: {roll_no}, Name: {name}, Marks: {marks}")

# One more example, so the pattern is clear:
student2 = (102, "Ali", 92)
roll_no2, name2, marks2 = student2
print(f"Roll No: {roll_no2}, Name: {name2}, Marks: {marks2}")
