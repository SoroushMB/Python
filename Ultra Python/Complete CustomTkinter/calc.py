from customtkinter import CTkButton,CTkEntry,CTkLabel,CTk,CTkToplevel,set_appearance_mode

def final_result():
    num1 = int(num1_ent.get())
    num2 = int(num2_ent.get())
    secondary_root = CTkToplevel()
    secondary_root.geometry("+500+200")
    result_lbl = CTkLabel(master=secondary_root ,text=f"Result: {num1+num2}" ,font=("JetBrains Mono",16) ,text_color="black" ,fg_color=("black", "gray75") ,corner_radius=12)
    result_lbl.grid(row=0 ,column=2 ,rowspan=2 ,sticky="nsew" ,padx=10 ,pady=10)
    secondary_root.mainloop()

set_appearance_mode(mode_string="dark")
root = CTk()
root.title("Calculator")

num1_lbl = CTkLabel(master=root ,text="Number1: " ,font=("JetBrains Mono",16) ,text_color="black" ,fg_color=("black", "gray75") ,corner_radius=12)
num2_lbl = CTkLabel(master=root ,text="Number2: " ,font=("JetBrains Mono",16) ,text_color="black" ,fg_color=("black", "gray75") ,corner_radius=12)

num1_ent = CTkEntry(master=root ,font=("JetBrains Mono",16) ,text_color="black" ,fg_color=("black", "gray75") ,corner_radius=12 ,show="*")
num2_ent = CTkEntry(master=root ,font=("JetBrains Mono",16) ,text_color="black" ,fg_color=("black", "gray75") ,corner_radius=12)

result_btn = CTkButton(master=root ,text="Tab to show!" ,font=("JetBrains Mono",16) ,text_color="black",hover_color=("#32a862") ,fg_color=("black", "gray75") ,corner_radius=12 ,command=final_result)

num1_lbl.grid(row=0 ,column=0 ,padx=10 ,pady=10)
num2_lbl.grid(row=1 ,column=0 ,padx=10 ,pady=10)

num1_ent.grid(row=0 ,column=1 ,padx=10 ,pady=10)
num2_ent.grid(row=1 ,column=1 ,padx=10 ,pady=10)

result_btn.grid(row=2 ,column=0 ,columnspan=2 ,padx=10 ,pady=10 ,sticky="ew")

root.mainloop()