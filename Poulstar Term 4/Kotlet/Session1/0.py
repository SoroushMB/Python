class iPhone_X:
    def __init__(self,owner_name:str,color:str,storage:int):
        self.owner_name = owner_name
        self.color = color
        self.storage = storage
        
    Display = ("OLED","5.83","1125*2436")
    CPU = "Apple A11 Bionic"
    RAM = "3GB LPDDR4"
    Camera = "12MP + 12MP"

Arad = iPhone_X(owner_name="Arad Shokouhi",color="Space Gray",storage=256)
print(Arad.owner_name)