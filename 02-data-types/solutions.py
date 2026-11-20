# solutions 02

# question 1
print(type(42))
print(type(3.14))
print(type("Python"))
print(type(True))
print(type(None))
print(type([1, 2]))
print(type((1, 2)))
print(type({"a": 1}))

# question 2
age_text = "25"
age = int(age_text)
print(age + 5)
age_str = str(age + 5)
print(type(age_str))

# question 3
score = 95
name = "Hassan"
price = 49.99
active = False
print(isinstance(score, int))
print(isinstance(name, str))
print(isinstance(price, int))
print(isinstance(active, bool))

# question 4
colours = ["red", "green", "blue"]
colours[1] = "yellow"
print(colours)
word = "hello"
word_upper = word.upper()
print(word)
print(word_upper)

# question 5
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("hello"))
print(bool([]))
print(bool([0]))
print(bool(None))
