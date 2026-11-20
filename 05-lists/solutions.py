# solutions 05

# question 1
fruits = ["apple", "banana", "mango", "orange"]
print(fruits)
print(fruits[0])
print(fruits[-1])
print(len(fruits))

# question 2
shopping = ["milk", "bread", "eggs"]
shopping.append("butter")
shopping.insert(1, "cheese")
shopping.remove("bread")
print(shopping)

# question 3
numbers = [5, 2, 9, 1, 7, 5, 2]
print(numbers.count(5))
print(numbers.index(9))
numbers.sort()
print(numbers)

# question 4
marks = [85, 90, 78, 92, 88]
sum = 0
for mark in marks:
    sum += mark
print("Total marks:", sum)
print("Average marks:", sum / len(marks))
# largest
max = marks[0]
for i in marks:
    if i > max:
        max = i
print('highest marks', max)
# smallest
min = marks[0]
for i in marks:
    if i < min:
        min = i
print("lowest number" , min )
marks.append(95)
marks.sort(reverse=True)
print(marks)
print("Top mark:", marks[0])

# question 5
squares = [n * n for n in [1, 2, 3, 4, 5]]
print(squares)
evens = [n for n in range(1, 11) if n % 2 == 0]
print(evens)
