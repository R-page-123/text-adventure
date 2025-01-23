res = input("input result as a percentage: ")
att = input("input attendance as a percentage: ")
if (att > 90) and (res >= 70):
    if res > 90:
        print("A")
    elif (res > 80) and (res <= 90):
        print("B")
    else:
        print("C")
else:
    print("Fail")