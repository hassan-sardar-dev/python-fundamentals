alpha = input("Enter a character: ")
if alpha.isdigit():
    print("The character is a digit.")
elif alpha.isalpha():
    print("The character is an alphabet.")
    if alpha.lower() in "aeiou":
        print("The character is a vowel.")
    else:
        print("The character is a consonant.")

