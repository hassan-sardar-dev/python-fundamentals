# solutions 04

# question 1
word = "Python"
print(word[0])
print(word[-1])
print(len(word))

# question 2
sentence = "I am learning Python"
print(sentence[:4])
print(sentence[-6:])
print(sentence[::-1])

# question 3
messy = "   hello WORLD   "
clean = messy.strip().lower()
print(clean)
print(clean.title())

# question 4
sentence = "apple banana mango orange"
fruits = sentence.split()
print(fruits)
print(" - ".join(fruits))

# question 5
def check_username(name):
    return name.strip().title() == "Hassan"

print(check_username("  hassan  "))
print(check_username("Hassan"))
print(check_username("Ali"))
