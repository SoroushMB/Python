from tkinter import Tk,Label,Button,Entry
# Relief : "ridge" , "raised" , "sunken" , "groove" , "flat" , "solid"
root = Tk()
root["bg"] = "#000000"
root.title("🤍-For test-🗿")
# root.geometry("500x400+00+00")
# root.resizable(1,1)

l1 = Label(master=root,
           text="Soroush Masoum Babaei",
           bg="#277da1",
           fg="#f94144",
           font=("JetBrains Mono",20),
           relief="ridge",
           border=20,
           anchor="w")

l2 = Label(master=root,
           text="09039851230",
           bg="#577590",
           fg="#f3722c",
           font=("JetBrains Mono",20),
           relief="ridge",
           border=20,
           anchor="w")

l3 = Label(master=root,
           text="21 Years Old",
           bg="#4d908e",
           fg="#f8961e",
           font=("JetBrains Mono",20),
           relief="ridge",
           border=20,
           anchor="center")
l1.grid(row=0,column=0,columnspan=2,rowspan=2,sticky="nsew")
l2.grid(row=0,column=2,sticky="nsew")
l3.grid(row=2,column=0,columnspan=3,sticky="nsew")
root.mainloop() 
