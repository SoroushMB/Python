from tkinter import Tk,Label,Button

counter = 50
def changer(clicker):
    global counter
    if clicker == "up":
        counter += 1
        temperature.config(text=f"Temp : {counter} °C")
    elif clicker == "down":
        counter -= 1
        temperature.config(text=f"Temp : {counter} °C")
    if counter < 60:
        cooler.config(text="Cooler Off")
    elif counter >= 60:
        cooler.config(text="Cooler On")

root = Tk()
root.config(background="#0b0f36")
temperature = Label(master=root,text="Temp : 50 °C",font=("Product Sans Medium",20),border=15,relief="raised",bg="#0b0f36",fg="skyblue")
cooler = Label(master=root,text="Cooler Off",font=("Product Sans Medium",20),border=15,relief="raised",bg="#0b0f36",fg="skyblue")
down = Button(master=root,text="👎",font=("Product Sans Medium",20),bg="#0bbaba",fg="#ffffff",command=lambda:changer(clicker="down"))
up = Button(master=root,text="👍",font=("Product Sans Medium",20),bg="#0bbaba",fg="#ffffff",command=lambda:changer(clicker="up"))

temperature.grid(row=0,column=0,padx=10,pady=10)
cooler.grid(row=0,column=1,padx=10,pady=10)
down.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")
up.grid(row=1,column=1,padx=10,pady=10,sticky="nsew")
root.mainloop()