def multiples(table, startnum, endnum, pupilname):
    print("hi", pupilname,"here are your times tables")
    endnum = endnum + 1
    for i in range(startnum,endnum):
        a = table * i
        print(table,"x",i,"=",a)




name = input("input name: ")
table = int(input("input table: "))
start = int(input("input start: "))
end = int(input("input end: "))

multiples(table, start, end, name)