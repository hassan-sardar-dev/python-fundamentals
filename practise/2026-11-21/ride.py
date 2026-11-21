# Fare = Rs 100 base + Rs 40 per km. At night (hour 22 or later, or before 6), add 20%. Take the km and the hour (0–23) and print the final fare. Test: 10 km at hour 23 → Fare: Rs 600.0
fare = int(input("Enter the fare amount: ")) + 40 * 10
hour = int(input("Enter the hour (0-23): "))
if hour >= 22 or hour < 6:
    fare *= 1.2
elif hour >= 6 and hour < 22:
    fare *= 1
else:
    print("Invalid hour input. Please enter an hour between 0 and 23.")
print("Fare: Rs", fare)