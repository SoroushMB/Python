# JSON = JavaScriptObjectNotation
# Dictionary = Object -> key:value = name:value
# List,Tuple = Array -> []
from json import load
from tkinter import Tk,Label,Frame
from tkinter.ttk import Notebook

with open("food.json","r") as main_file:
    foods = load(main_file)

foods_names = tuple(foods.keys()) # Tabs Titles
root = Tk()

main_part = Notebook(master=root)
first_tab = Frame(master=main_part,width=500,height=500)
second_tab = Frame(master=main_part,width=500,height=500)
third_tab = Frame(master=main_part,width=500,height=500)

first_tab.pack()
second_tab.pack()
third_tab.pack()
main_part.pack()

main_part.add(child=first_tab,text=f"{foods_names[0]}")
main_part.add(child=second_tab,text=f"{foods_names[1]}")
main_part.add(child=third_tab,text=f"{foods_names[2]}")

root.mainloop()