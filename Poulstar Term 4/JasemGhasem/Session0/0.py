# Object-Oriented Programming(OOP)
from datetime import date

class iPhone_SE_2020:
    # Initializer Function
    def __init__(self,owners_name:str,capacity:int,color:str):
        self.owners_name = owners_name
        self.capacity = capacity
        self.color = color

    def ownership(self):
        current_date = date.today()
        return (self.owners_name , current_date , self.capacity, self.color)
    
    display = (4.7,"IPS LCD(Retina)","1334*750")
    chipset = "Apple A13 Bionic"
    RAM = ("3GB","LPDDR4")
    storage = "NVMe SSD"
    battery = "1821 mAh"

soroush = iPhone_SE_2020(owners_name="Soroush MasoumBabaei",capacity=128,color="Red")
result = soroush.ownership()
print(f"{result[0]} has bought an iPhone in the time {result[1]}")