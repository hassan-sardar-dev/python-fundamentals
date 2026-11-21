matric_number = int(input("Enter your matric number: "))
inter_number = int(input("Enter your intermediate number: "))
enter_number = int(input("Enter your entrance exam number: "))
if matric_number >=60 and inter_number >50 and enter_number >=70:
    print("You are eligible for admission.")
else:
    print("You are not eligible for admission.")