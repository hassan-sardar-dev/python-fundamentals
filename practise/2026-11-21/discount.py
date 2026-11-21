price = int(input("Enter the price of the item: "))
if price <= 5000:
    discount = price * 0.10
    final_price = price - discount
    print("Discount: Rs.", discount)
    print("Final Price: Rs.", final_price)
elif price > 2000 and price <= 4999:
    discount = price * 0.20
    final_price = price - discount
    print("Discount: Rs.", discount)
    print("Final Price: Rs.", final_price)
else:
    discount = price * 0.30
    final_price = price - discount
    print("Discount: Rs.", discount)
    print("Final Price: Rs.", final_price)
    
    