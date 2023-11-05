from tkinter import Tk,Label,Button,Entry,LabelFrame
from PIL import ImageTk
from customturtle import Shapes

style_configuration = {
    "lbls" : {
        "bg":"#240046",
        "fg":"#ff9e00",
        "font":("JetBrains Mono",16),
        "relief":"raised",
        "border":20,
        "anchor":"w",
    },
    "ents" : {
        "bg":"#9d4edd",
        "fg":"#ff9100",
        "font":("JetBrains Mono",16),
        "relief":"sunken",
        "border":20
    }
}
grid_configurations = {
    1 : {"row":0,"column":0,"sticky":"nsew"},
    2 : {"row":1,"column":0,"sticky":"nsew"},
    3 : {"row":2,"column":0,"sticky":"nsew"},
    4 : {"row":3,"column":0,"sticky":"nsew"},
    5 : {"row":4,"column":0,"sticky":"nsew"},
    6 : {"row":5,"column":0,"sticky":"nsew"}
}
root = Tk()
root.title("Shape Maker")
# root.iconphoto(default=False,)

shapes_lf = LabelFrame(master=root,text="Shapes Kinds")
fdis_lf = LabelFrame(master=root,text="First District")
sdis_lf = LabelFrame(master=root,text="Second District")

triangle_lbl = Label(master=shapes_lf,text="Triangle",cnf=style_configuration["lbls"])
square_lbl = Label(master=shapes_lf,text="Square",cnf=style_configuration["lbls"])
rectangle_lbl = Label(master=shapes_lf,text="Rectangle",cnf=style_configuration["lbls"])
penta_lbl = Label(master=shapes_lf,text="Pentagon",cnf=style_configuration["lbls"])
hex_lbl = Label(master=shapes_lf,text="Hex",cnf=style_configuration["lbls"])
custom_lbl = Label(master=shapes_lf,text="Custom Shape",cnf=style_configuration["lbls"])

triangle_ent = Entry(master=fdis_lf,cnf=style_configuration["ents"])
square_ent = Entry(master=fdis_lf,cnf=style_configuration["ents"])
rectangle_ent = Entry(master=fdis_lf,cnf=style_configuration["ents"])
penta_ent = Entry(master=fdis_lf,cnf=style_configuration["ents"])
hex_ent = Entry(master=fdis_lf,cnf=style_configuration["ents"])
custom_ent = Entry(master=fdis_lf,cnf=style_configuration["ents"])

shapes_lf.grid(row=0,column=0,sticky="nsew")
fdis_lf.grid(row=0,column=1,sticky="nsew")
sdis_lf.grid(row=0,column=2,sticky="nsew")

triangle_lbl.grid(cnf=grid_configurations[1])
square_lbl.grid(cnf=grid_configurations[2])
rectangle_lbl.grid(cnf=grid_configurations[3])
penta_lbl.grid(cnf=grid_configurations[4])
hex_lbl.grid(cnf=grid_configurations[5])
custom_lbl.grid(cnf=grid_configurations[6])

triangle_ent.grid(cnf=grid_configurations[1])
square_ent.grid(cnf=grid_configurations[2])
rectangle_ent.grid(cnf=grid_configurations[3])
penta_ent.grid(cnf=grid_configurations[4])
hex_ent.grid(cnf=grid_configurations[5])
custom_ent.grid(cnf=grid_configurations[6])
root.mainloop()