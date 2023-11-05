from tkinter import Tk,Label,Button,Entry
# Relief : "ridge" , "raised" , "sunken" , "groove" , "flat" , "solid"
root = Tk()
root["bg"] = "#000000"
root.title("🤍-For test-🗿")
root.geometry("500x400+00+00")
# root.resizable(1,1)

l1 = Label(master=root,
           text="Hello, World!",
           bg="blue",
           fg="darkred",
           font=("Bauhaus 93",20),
           relief="ridge",
           border=20)
l1.pack()
root.mainloop()
