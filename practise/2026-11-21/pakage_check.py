pakage = int(input("Enter the package price: "))
balance = int(input("Enter the balance amount: "))
if balance >= pakage:
    print("You can buy the package.")
else:
    print("You cannot buy the package. You need", pakage - balance, "more to buy the package.") 