# Arash : Image
# Aria : Toplevel
# Parmis : Toplevel Opening
# Aryo : Creating label & using eval()
# Variables : name = value
number = 526
from tkinter import Tk,Label,Button,Entry,Checkbutton,Radiobutton,Toplevel,IntVar,StringVar

def delkhahi():
    yevari_result = yevari.get()
    yevari_jadid_result = yevari_jadid.get()
    
    if yevari_result == 2:
        print("Boro")
    elif yevari_result == 10:
        print("Bia")
    if yevari_jadid_result == "Aria":
        print("Unvari")
root = Tk()
root.geometry("600x400")

yevari = IntVar()
yevari_jadid = StringVar()
cb1 = Checkbutton(root,text="Salam",offvalue=2,onvalue=10,variable=yevari,command=delkhahi())
rb1 = Radiobutton(root,text="Hallo",value="Aria",variable=yevari_jadid,command=delkhahi())

cb1.pack()
rb1.pack()

root.mainloop()