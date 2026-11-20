# exercise 5: find even and odd numbers from the list
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
even_num =[]
odd_num = []
for num in num_list:
    if num % 2 == 0:
        even_num.append(num)
        
    else:
        odd_num.append(num)
print("Even numbers:", even_num)
print("Odd numbers:", odd_num)
