def temp():
    t = input("do you have a temperature? ")
    if t == "y":
        return True
    else:
        return False
def soreT():
    s = input("do you have a sore throat")
    if s =="y":
        return True
    else:
        return False
def cough():
    t = input("do you have a cough? ")
    if t == "y":
        return True
    else:
        return False



if temp() == True:
    if soreT() == True:
        print("you may have a throat infection")
    elif cough() == True:
        print("you may have a chest infection")
    else:
        print("you have a feaver")
else:
    print("we cant help")