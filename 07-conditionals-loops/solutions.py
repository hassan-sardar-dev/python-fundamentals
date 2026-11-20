# solutions 07

# question 1
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# question 2
marks = int(input("Enter your marks (0-100): "))
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("F")

# question 3
for n in range(1, 11):
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")

# question 4
total = 0
number = int(input("Enter a number (0 to stop): "))
while number != 0:
    total = total + number
    number = int(input("Enter a number (0 to stop): "))
print("Total:", total)

# question 5
words = ["cat", "elephant", "dog", "giraffe", "ant"]
for word in words:
    if len(word) > 5:
        print(word)
        break
else:
    print("No long word found.")
