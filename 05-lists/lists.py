# lists

# question 1) print the first , last and the 3 from the middle cities 
cities = ["Lahore", "Karachi", "Multan", "Quetta", "Peshawar"] 
print(cities[0], cities[-1], cities[1:4])  
# reverse cities  
cities.reverse()
print(cities)

# indexing
fruits = ["apple", "banana", "mango", "orange"]
print(fruits[0])
print(fruits[1])
print(fruits[-1])
print(fruits[-2])

# slicing
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[::-1])

# len and in
fruits = ["apple", "banana", "mango"]
print(len(fruits))
print("banana" in fruits)
print("grapes" in fruits)

# change item
fruits = ["apple", "banana", "mango"]
fruits[1] = "grapes"
print(fruits)

# question 2: find total , average , highest and lowest marks 
# total 
marks = [78, 92, 65, 88, 54]
sum = 0
for mark in marks:
    sum += mark
print("Total marks:", sum)
# average 
marks_two = [78, 92, 65, 88, 54]
sum2 = 0
for mark in marks_two:
    sum2 += mark
average = sum2 / len(marks_two)
print("Average marks:", average)

# largest 
marks_three = [78, 92, 65, 88 , 54]
max = marks_three[0]
for i in marks_three:
    if i > max:
        max = i
print('highest marks', max)

# smallest 
marks_four = [78 , 92 , 65, 88 , 54]
min = marks_four[0]
for i in marks_four:
    if i < min:
        min = i
print("lowest number" , min )

# greather then 70
marks_five = [78 , 92 , 65, 88 , 54]
for i in marks_five:
    if i >= 70:
      print('greater', i)

# shopping list 
shopping_list = ["bread", "milk", "eggs"]
shopping_list.append('rice')
print(shopping_list)
shopping_list.insert(1, 'suggar')
print(shopping_list)
shopping_list.remove('milk')
print(shopping_list)
shopping_list.pop()
print(shopping_list)

# sort and reverse
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers.reverse()
print(numbers)

# copy
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)
print(list2)

list1 = [1, 2, 3]
list2 = list1.copy()
list2.append(4)
print(list1)
print(list2)

# nested list
students = [["Hassan", 85], ["Ali", 90], ["Sara", 78]]
print(students[0])
print(students[0][0])
print(students[1][1])

# loop in list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# level 2
num = [3, 1, 3, 2, 1, 5] 
seen = []
for i in num:
    if i in seen:
        print(i)
    else:
        seen.append(i)
