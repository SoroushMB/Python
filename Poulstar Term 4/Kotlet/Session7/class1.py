class Human:
    def __init__(self,Name,Age,HairColor):
        self.Name = Name
        self.Age = Age
        self.HairColor = HairColor
        
    def __str__(self):
        return f"{self.Name} is {self.Age} years old"
    
    def Actions(self):
        return {"Moving":True,"Fly":False}


FirstHuman = Human(Name="S",Age=21,HairColor="Black")
Abilities = FirstHuman.Actions()
print(Abilities["Moving"])