# excercise 7: copy of the list 
a = [1, 2, 3]
b = a
c = a.copy()
a.append(4)
print("a:", a)
print("b:", b)
print("c:", c)
# b changed because it is a shallow copy of a, while c is a deep copy and remains unchanged.
