# OOP : Object-Oriented Programming
# Class , Instance : Object
# White Board --> Attributes : Variable(Property) , Function(Method)
# Dimensions , Materials
class White_Board:
    
    def __init__(self,height:int,width:int,depth:int):
        self.height = height
        self.width = width
        self.depth = depth

    def whiteness(self):
        if self.height > 50:
            return 60
        else:
            return 75

    material = "Fiber Glass"
    magnets = True


poulstar_orange_room = White_Board(height=150,width=90,depth=8)
print(f"The whiteness is {poulstar_orange_room.whiteness()}%")