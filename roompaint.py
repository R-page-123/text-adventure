totalH = int(input("what is the height of the room: "))
totalL = int(input("what is the total length of the room (the with of each wall added up): "))
coats = int(input("how many coats: "))
unpH = int(input("total height of the unpaintable areas: "))
unpL = int(input("total length of the unpainable areas: "))

total = totalH * totalL
total = total * coats
unpT = unpH * unpL
total = total - unpT
print(total)