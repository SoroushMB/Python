from tkinter import Tk,Label,Button,Entry

root = Tk()
root.geometry("600x500+0+0")
root.title(string="Team Cena")
root["bg"] = "#b8c0ff"

greeting1 = Label(master=root, text="Hello, World!", font=("Bodoni MT",22), bg="#b8c0ff", fg="#3d348b", relief="ridge", border=40)
greeting2 = Label(master=root, text="Hello, World!", font=("Bodoni MT",22), bg="#b8c0ff", fg="#3d348b", relief="raised", border=40)
greeting3 = Label(master=root, text="Hello, World!", font=("Bodoni MT",22), bg="#b8c0ff", fg="#3d348b", relief="groove", border=40)
greeting4 = Label(master=root, text="Hello, World!", font=("Bodoni MT",22), bg="#b8c0ff", fg="#3d348b", relief="solid", border=40)
greeting5 = Label(master=root, text="Hello, World!", font=("Bodoni MT",22), bg="#b8c0ff", fg="#3d348b", relief="flat", border=40)
greeting6 = Label(master=root, text="Hello, World!", font=("Bodoni MT",22), bg="#b8c0ff", fg="#3d348b", relief="sunken", border=40)
greeting1.pack()
greeting2.pack()
greeting3.pack()
greeting4.pack()
greeting5.pack()
greeting6.pack()
root.mainloop()