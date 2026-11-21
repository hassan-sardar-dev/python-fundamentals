side1 = int(input("Enter the first side: "))
side2 = int(input("Enter the second side: "))
side3 = int(input("Enter the third side: "))
if side1 == side2 == side3:
    print("The triangle is equilateral.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is isosceles.")
elif side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
    print(" Not a valid triangle")
else:
    print("The triangle is scalene.")