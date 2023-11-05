from tkinter import Button,Label,Tk
from tkinter.ttk import Notebook


class Guilan:

    def __init__(self,name:str,population:int=1_000,area:int=500):
        self.first_name = name
        self.population = population
        self.area = area

    humidity = "High"
    sub_language = "Guilaki"

first_city = Guilan(name="Roudsar",area=2300)
print(first_city.area)