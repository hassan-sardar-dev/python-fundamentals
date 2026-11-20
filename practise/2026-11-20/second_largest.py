# excerise 11 second largest number from the list
scores = [45, 82, 67, 91, 73] 
maxnumber = 0
secondmax = 0
for i in scores:
    if i > maxnumber:
        secondmax = maxnumber
        maxnumber = i
        print("max", maxnumber) # it will takes the first number on 0 index as max and then it will moves on ward  and find more max then this number
    elif i > secondmax and i != maxnumber:
        secondmax = i
        print("secondmax", secondmax) # it will takes the second largest number and then it will moves on ward  and find more second largest then this number
print("Second largest score:", secondmax)
