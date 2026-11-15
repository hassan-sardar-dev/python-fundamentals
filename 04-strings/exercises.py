"""Lesson 04 - Strings: Exercises.

Run: python3 exercises.py
Try each exercise yourself. Do NOT look at solutions.py until you have tried.
"""

print("--- Exercise 1: First and last letters ---")
# Create word = "Python".
# Print the first letter, the last letter, and the length of the word.
# (Use indexing and len().)


print("--- Exercise 2: Slice a sentence ---")
# Create sentence = "I am learning Python".
# Print the first 4 characters, the last 6 characters,
# and the whole sentence reversed.
# (Use slicing. The reversed sentence is "nohtyP gninrael ma I".)


print("--- Exercise 3: Clean up user input ---")
# A user typed: messy = "   hello WORLD   "
# Clean it up: remove the spaces from both ends and make it lower case.
# Print the result — it should be "hello world".
# Then print it again in title case: "Hello World".


print("--- Exercise 4: Split and join ---")
# Create sentence = "apple banana mango orange".
# Split it into a list of fruits and print the list.
# Then join the fruits back together with " - " between them
# and print the result: "apple - banana - mango - orange".


print("--- Exercise 5: Username checker ---")
# Write a function check_username(name) that returns True if the name,
# after removing spaces and fixing the case, is "Hassan", else False.
# (Hint: name.strip().title() == "Hassan")
# Test it with these three names and print each result:
# "  hassan  "  -> True
# "Hassan"       -> True
# "Ali"          -> False
