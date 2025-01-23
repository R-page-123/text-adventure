def emptyCarPark():
    carPark = [["empty","empty","empty","empty","empty","empty","empty","empty","empty","empty",],
            ["empty","empty","empty","empty","empty","empty","empty","empty","empty","empty",],
            ["empty","empty","empty","empty","empty","empty","empty","empty","empty","empty",],
            ["empty","empty","empty","empty","empty","empty","empty","empty","empty","empty",],
            ["empty","empty","empty","empty","empty","empty","empty","empty","empty","empty",],
            ["empty","empty","empty","empty","empty","empty","empty","empty","empty","empty",]]
    return carPark

def parkACar(carPark):
    car = input("enter reg ")
    col = int(input("enter column "))
    row = int(input("enter row "))
    if carPark[col][row] != "empty":
        oldc = col
        oldr = row
        while (oldc == col) and (oldr == row):

            col = int(input("full input new colmn "))
            row = int(input("input new row "))
    carPark[col][row] = car
    return carPark

def removeACar(carPark):
    col = int(input("enter column "))
    row = int(input("enter row "))
    carPark[col][row] = "empty"

def displayCarParkGrid(carPark):
    print(carPark)

carp = emptyCarPark()

option = "0"

while option != "5":
    print("1. Reset all spaces in the car park to 'empty'")
    print("2. Park a car")
    print("3. Remove a car")
    print("4. Display the car park grid")
    print("5. Quit\n")
    option = input("Enter your choice: ")
    if option == "1":
        carp = emptyCarPark()
        option = "0"
    elif option == "2":
        carp = parkACar(carp)
        option = "0"
    elif option == "3":
        removeACar(carp)
        option = "0"
    elif option == "4":
        displayCarParkGrid(carp)
        option = "0"
    else:
        
        print("invalid")