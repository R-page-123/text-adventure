def evcheck(num):
    if num % 2 == 0:
        return True
    else:
        return False


sweet = int(input("how meany sweets "))
bags = int(input("how meany bags "))
sweeteven = evcheck(sweet)
bageven = evcheck(bags)

if (sweeteven == True and bageven == True) or (sweeteven == False and bageven == False):
    print("place 1 sweet in", bags-1, "bags and in the last bag place the remaining", sweet-(bags-1))
else:
    print("this is not posible!")

