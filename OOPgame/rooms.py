class Room():
    def __init__(self,room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
    def SETlinked(self, nextroom, direction):
        self.linked_rooms[direction] = nextroom
    def SETdescription(self, description):
        self.description = description
    def GETdescription(self):
        return self.description
    def GETname(self):
        return  self.name
    def GETdetails(self):
        print("you are in the", self.GETname())
        print("it is", self.GETdescription())
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("the", room.GETname(), "is to the",direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("you cant go that way")
            return self
    
    def SETcharacter(self,chara):
        self.character = chara
    def GETcharacter(self):
        return self.character
    