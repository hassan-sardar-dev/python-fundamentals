# strings

# quotes
single = 'hello'
double = "hello"
triple = """hello"""
print(single, double, triple)
sentence = "It's a nice day"
print(sentence)
message = """Hello,
this is line two,
and this is line three."""
print(message)

# indexing
word = "Python"
print(word[0])
print(word[1])
print(word[-1])
print(word[-2])

# slicing
line = "This is a sample line of text"
print(line[0])
print(line[5:10])
print(line[-5:])
print(line[:4])
print(line[5:])
print(line[:])
print(line[::2])
print(line[::-1])

# join and repeat
first = "Hassan"
last = "Sardar"
print(first + " " + last)
print("Ha" * 3)
print("-" * 20)
age = 20
print("Age: " + str(age))
print("Age:", age)

# len and in
name = "Hassan"
print(len(name))
print("H" in name)
print("z" in name)
print("z" not in name)
print("ass" in name)

# f string
name = "Hassan"
age = 20
print("My name is", name, "and I am", age, "years old.")
print("Next year I will be", age + 1)
print("My name in upper case is", name.upper())

# escape
print("Hello\nWorld")
print("Name:\tHassan")
print("C:\\Users\\Hassan")
print('He said "Hi"')
print("It's fine")

# upper lower etc
word = "hello"
print(word.upper())
print(word)
word = word.upper()
print(word)

name = 'my name is hassan'
print(name)
print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())
print("HELLO".casefold())

# strip
print("  hi  ".strip())
print("  hi  ".lstrip())
print("  hi  ".rstrip())

# split and join
print(name.split(" "))
print("a b c".split())
print("a,b,c".rsplit(",", 1))
print("-".join(["a", "b"]))
print(", ".join(["apple", "banana", "mango"]))

# find and replace
print(line.replace("sample", "test"))
print(line.find("line"))
print(line.index("line"))
print(line.count("is"))
print("hello".startswith("he"))
print("hello".endswith("lo"))
print("hello".find("z"))

# check
print("abc".isalpha())
print("ab1".isalpha())
print("123".isdigit())
print("12a".isdigit())
print("abc123".isalnum())
print("ab c".isalnum())
print("   ".isspace())
print(" a ".isspace())

# my first string examples
age = 20
print('My name is', name, 'and I am', age, 'years old')
print(line[0])
print(line[5:10])
print(line[-5:])
print(line.replace("sample", "test"))
print(line.find("line"))
print(line.count("is"))

# username check
def username(name):
    if name == "Hassan":
        return "This is valid username"
    else:
        return "This is not a valid username"

print(username("Hassan"))
print(username("Ali"))

def check_username(name):
    return name.strip().title() == "Hassan"

print(check_username("  hassan  "))
print(check_username("Ali"))
