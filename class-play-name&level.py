Name = input("Please enter the name: ")
Level = input("Please enter the level ")

class Player:
    def __init__(self, name, level):
       self.name = name
       self.level = level
    
    def intro(self):
        print(self.name +"\n","Level: " + self.level +"")


Info=Player(Name, Level)
Info.intro()
