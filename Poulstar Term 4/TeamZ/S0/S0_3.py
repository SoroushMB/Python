# Attributes : Property(Variable) , Function(Methods)
# Initialize
# Human
class MP4_12C:

    def __init__(self,name,color):
        self.name = name
        self.color = color

    Engine = ("V8",3.8)
    Aspiration = "Twin-Turbo"
    Rims = "BBS (10)"
    Spoiler = "Aerodynamic"
    Gas_Tank = "60 Liter"

    def speed(self):
        return "330 KM/h"

    def ownership(self):
        return self.name , self.color

avesta = MP4_12C(name="Avesta MirSaeidi",color="Blue")
print(avesta.Engine)
print(f"The owner of this car is {avesta.ownership()}")