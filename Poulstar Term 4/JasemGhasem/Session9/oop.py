"""
Object-Oriented Programming -> Human ==> 
                                        In Common :2 Eyes, 2 Hands, 2 Legs
                                        Different :Name, Hair Color, Age
"""
class Human:
    def __init__(self, Name:str, HairColor:str, Age:int):#Method
        self.Name = Name
        self.HairColor = HairColor
        self.Age = Age
        
    InCommons = ["2 Eyes","2 Hands","2 Legs"]#Property
    
    def hamintori(self):
        return "Alaki"
    
first = Human(Name="Sadra",Age=980,HairColor="Platinum Blonde")
print(first.Name,first.Age,first.hamintori())