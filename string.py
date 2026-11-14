name = 'my name is hassan'
print(name)
print(name.upper())
print(name.lower())
print(name.title())   #to captalize the first letter of each word
print(name.capitalize())  #to captalize the first letter of the string
print(name.split(" "))  #to split the string into a list of words

age = 20
print(f'My name is {name} and I am {age} years old')  #f-string formatting

line = "This is a sample line of text"
print(line[0])
print(line[5:10])  #slicing the string from index 5 to 10
print(line[-5:])  #slicing the string from index -5 to the end
print(line.replace("sample", "test"))  #replacing a word in the string
print(line.find("line"))  #finding the index of a word in the string
print(line.count("is"))  #counting the number of occurrences of a word in the string