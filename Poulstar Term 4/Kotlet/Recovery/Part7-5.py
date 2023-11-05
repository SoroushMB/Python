from turtle import fd,lt,rt,done

class Human:
    InCommon = ["2 Eyes","2 Legs","2 Hands"]
    def __init__(self,Name,Age,HairColor):
        self.Name = Name
        self.Age = Age
        self.HairColor = HairColor
    
    def Driving(self):
        if self.Age >= 18:
            return "Legal"
        else:
            return "Illegal"

First = Human(Name="Mahan",Age=16,HairColor="DarkBrown")
print(First.Name)
print(First.Driving())