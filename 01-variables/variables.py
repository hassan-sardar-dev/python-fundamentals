# variables

# question 1
name = "Hassan"
age = 20
print(name)
print(age)

# using variables
city = "Lahore"
price = 150
print(city)
print("Price:", price)

apples = 5
oranges = 3
total = apples + oranges
print(total)
print("I have", total, "fruits.")

# naming rules
user_name = "Hassan"
age2 = 20
_private = 1
print(user_name, age2, _private)
# capital letter is different variable
Age = 30
AGE = 40
print(age, Age, AGE)

# multiple assignment
x, y, z = 1, 2, 3
print(x, y, z)
a = b = c = 0
print(a, b, c)

# swap
a = 5
b = 10
print("Before swap:", a, b)
a, b = b, a
print("After swap:", a, b)

# reassign
score = 10
print(score)
score = 25
print(score)
score = score + 5
print(score)

# same variable, different type
data = 100
print(data, type(data))
data = "hello"
print(data, type(data))
data = 3.5
print(data, type(data))

# constants
PI = 3.14159
MAX_USERS = 100
print(PI)
print(MAX_USERS)

# print with variables
name = "Hassan"
age = 20
print("My name is", name, "and I am", age, "years old.")
print("My name is", name, "and I am", age, "years old.")
print("Next year", name, "will be", age + 1)

# input example, try it yourself
# name = input("Enter your username: ")
# print("Hello,", name)
