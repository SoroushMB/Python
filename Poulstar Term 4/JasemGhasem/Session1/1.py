# Surface
# OOP(Object-Oriented Programming)
# Attributes -> Variable(Property) , Function(Method)
from datetime import date

class Surface_Laptop_4:
    
    def __init__(self,owner_name:str,color:str,ram:int,storage:int,cpu:str):
        self.owner_name = owner_name
        self.color = color
        self.ram = ram
        self.storage = storage
        self.cpu = cpu
    
    def certificate(self):
        return (self.owner_name,date.today()) 

    def pricing(self):
        self.extra_cost = 0
        
        if self.storage == 128:
            self.extra_cost = 0
        elif self.storage == 256:
            self.extra_cost += 100
        elif self.storage == 512:
            self.extra_cost += 200
        elif self.storage == 1024:
            self.extra_cost += 400
            
        if self.ram == 8:
            self.extra_cost = 0
        elif self.ram == 16:
            self.extra_cost += 100
        elif self.ram == 32:
            self.extra_cost += 200


        if self.cpu == "i3":
            self.extra_cost = 0
        elif self.cpu == "i5":
            self.extra_cost += 150
        elif self.cpu == "i7":
            self.extra_cost += 300
            
        return 699.99 + self.extra_cost
            
    body = "Magnesium Alloy"
    cpu_manufacture = "Intel"
    RAM_storage = (8,16,32)
    main_storage = (128,256,512,1024)
    cpu_series = "12th Gen Core-i Series"
    colors = ("Sandstone","Platinum","Matte Black","Ice Blue")
    starting_price = 699.99

first_laptop = Surface_Laptop_4(owner_name="Shamin Ghavami",color="Matte Black",ram=16,storage=512,cpu="i7")
second_laptop = Surface_Laptop_4(owner_name="Alireza Azizi",color="Platinum",ram=32,storage=1024,cpu="i7")
print(first_laptop.certificate())