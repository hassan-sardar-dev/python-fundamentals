temp = int(input("Enter the temperature"))
if temp > 35:
    print("Very hot, stay hydrated")
elif temp >= 26 and temp <= 35:
    print("Warm")
elif temp >=10 and temp <= 25:
    print("Pleasant")
else:
    print("Cold")