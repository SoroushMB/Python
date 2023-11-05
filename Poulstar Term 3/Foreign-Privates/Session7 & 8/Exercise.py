from tkinter import Tk,Button

def colorizer(color):
    if color == "Dark Purple":
        window.config(background="#3d348b")
    elif color == "Light Purple":
        window.config(background="#7678ed")
    elif color == "Light Orange":
        window.config(background="#f7b801")
    elif color == "Normal Orange":
        window.config(background="#f35b04")

window = Tk()
window.title("Color Changer!")
window.geometry("500x450")

dark_purple_color = Button(master=window,text="Dark Purple",bg="#3d348b",font=("JetBrains Mono",16),relief="raised",border=20,width=16,command=lambda:colorizer(color="Dark Purple"))
light_purple_color = Button(master=window,text="Light Purple",bg="#7678ed",font=("JetBrains Mono",16),relief="raised",border=20,width=16,command=lambda:colorizer(color="Light Purple"))
light_orange_color = Button(master=window,text="Light Orange",bg="#f7b801",font=("JetBrains Mono",16),relief="raised",border=20,width=16,command=lambda:colorizer(color="Light Orange"))
normal_orange_color = Button(master=window,text="Normal Orange",bg="#f35b04",font=("JetBrains Mono",16),relief="raised",border=20,width=16,command=lambda:colorizer(color="Normal Orange"))

dark_purple_color.grid(row=0 ,column=0)
light_purple_color.grid(row=0 ,column=1)
light_orange_color.grid(row=1 ,column=0)
normal_orange_color.grid(row=1 ,column=1)

window.mainloop()