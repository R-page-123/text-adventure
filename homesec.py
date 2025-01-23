
#  the first section 

moveG = input("groundfloor movement? (y/n)")
moveF = input("first floor movement? (y/n)")
alarm = False
trigger = input("triger on?(y/n)")
if trigger == "ON":
    if moveG == "y":
        print("alarm ground floor")
        alarm = True
    if moveF == "y":
        print("alarm first floor")
        alarm = True


# the second section 

if (moveG == "y" or moveF == "y")and trigger == "ON":
    alarm = True
    print("Intruder Alert!")

