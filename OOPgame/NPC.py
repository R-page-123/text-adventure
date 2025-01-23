class Character():
    def __init__(self, myname, mydes):
        self.name = myname
        self.description = mydes
        self.conversation = None
    def describe(self):
        print(self.name, "is here")
        print(self.description)
    def SETconvo(self,convo):
        self.conversation = convo
    def talk(self):
        if self.conversation is not None:
            print(self.conversation)
        else:
            print(self.name, "dosent want to talk")