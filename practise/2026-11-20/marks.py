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
greater = marks_five[0]
for i in marks_five:
    if i >= 70:
      print('greater', i)
