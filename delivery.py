order = float(input("total value of your order: "))
next = input("do you want next day delivery (y/n)  ")

order = round(order,2)
second = 3.50
first = 5.00
if next == "y":
    order = order + first
    print("charge:",order,"delivery fee (added on):",first)
else:
    if (order >= 15.00):
        print("charge:",order,"delivery fee:")
    elif (order < 15.00):
        order = order + second
        print("charge:",order,"delivery fee (added on):",second)