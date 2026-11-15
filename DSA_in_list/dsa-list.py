# find the max in the list with out max function
num = [1,2,3,4,5,6,7,8,9,10, 23, 2134, 23, 32, 323, 88 , 97]
max= num[0]
for i in num:
    if i> max:
        max = i
print(max)

# find the min in the list with out min function
num2 = [23, 2134, 23, 32, 323, 88 , 97]
min = num2[0]
for i in num2:
    if i< min:
        min = i
print(min)

# find the sum of all items in the list with out sum function
num3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum =0
for i in num3:
    sum+=i
print(sum)

# find the even numbers in the list with out using any function
num4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in num4:
    if i%2==0:
        print(i)

