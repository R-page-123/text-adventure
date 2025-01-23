print("economy")
print("saloon")
print("sports")
car = input("which would you like?: ")

def conf(carname):
    con = input("(press y to confirm): ")
    if con == "y":
        print(carname,"confirmed have a nice day")
    else:
        print(carname,"not confirmed have a nice day")


match car:
    case "economy":
        conf("economy")
    case "saloon":
        conf("saloon")
    case "sports":
        conf("sports")
    case _:
        print("invalid")