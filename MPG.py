lastm = int(input("car mileage when last filled"))
nowm = int(input("car milage now"))
ltf = float(input("num of litres to fill tank"))
miles = nowm - lastm
g = ltf * 0.264172
mpg = miles / g 
print(mpg)