"""
Windows : CTk,CTkToplevel
Widgets : CTkLabel
Layouts : Pack
"""
from customtkinter import CTk,CTkLabel,set_appearance_mode
from tkinter import StringVar


set_appearance_mode(mode_string="light")
# ------Windows------
first_page = CTk()
first_page.geometry("+300+300")
first_page.title("Hi🗿")

# ------Widgets------
teacher_name_tag = CTkLabel(master=first_page,text="Soroushi",font=("JetBrains Mono",32),text_color="black",fg_color=("black", "gray75"),corner_radius=18)
student_name_tag = CTkLabel(master=first_page,text="AmirTaha",font=("JetBrains Mono",32),text_color="black",fg_color=("black", "gray75"),corner_radius=18)


# ------Layout------
student_name_tag.grid(row=0,column=1,padx=10,pady=10)
teacher_name_tag.grid(row=1,column=1,padx=10,pady=10)
first_page.mainloop()