from tkinter import Canvas,Tk
from PIL import Image,ImageTk

main_win = Tk()
main_win.geometry("750x270")

main_canvas = Canvas(master=main_win, width=600, height=400)
saturn_image = Image.open(r"C:\Users\DELL\Downloads\simon-lee-z1vpjHAq1o8-unsplash.jpg")

resized_image = saturn_image.resize((300,255), Image.LANCZOS)
new_image = ImageTk.PhotoImage(resized_image)

main_canvas.create_image(10, 10, anchor="nw", image = new_image)
main_canvas.pack()

main_win.mainloop()