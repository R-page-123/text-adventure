from rooms import Room
from NPC import Character

commands = ["north", "south", "east","west", "talk"]
#inits 
Kitchen = Room("kitchen")
DiningRoom = Room("dining room")
BallRoom = Room("ball room")
Balcony = Room("balcony")
dave = Character("dave", "a smelly zobie")
gordon = Character("gordon", "an idiot sandwitch")
myles = Character("myles bell", "holding a guitar with his grippers")
#setters

dave.SETconvo("...")
gordon.SETconvo("this is raw!!")
myles.SETconvo("im so confused right now, i dont know what is going on")

Kitchen.SETdescription("a normal looking kitchen")
Kitchen.SETlinked(DiningRoom, "south")
Kitchen.SETcharacter(gordon)

DiningRoom.SETdescription("a standard dining room with a large table")
DiningRoom.SETlinked(Kitchen, "north")
DiningRoom.SETlinked(BallRoom, "west")

BallRoom.SETlinked(DiningRoom, "east")
BallRoom.SETlinked(Balcony, "north")
BallRoom.SETdescription("a large room with grand decorations")
BallRoom.SETcharacter(myles)

Balcony.SETlinked(BallRoom, "south")
Balcony.SETdescription("a balcony overlooking a great view")
Balcony.SETcharacter(dave)
current_room = Kitchen

while True:
    print("\n")
    current_room.GETdetails()

    npc = current_room.GETcharacter()
    if npc is not None:
        npc.describe()
    command = input("> ").lower()
    if command in ["north", "south", "east","west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if npc is not None:
            npc.talk()
        else:
            print("you are talking to yourself")
    else:
        print("you have not entered a valid command")
        print("these are the commands you can use:")
        for c in commands:
            print(c)
