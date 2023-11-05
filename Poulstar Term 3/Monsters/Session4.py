from tkinter import Tk,Entry,Button,Toplevel,Label
from tkinter.messagebox import showinfo
from json import dump,load

def calculate():
    number1 = int(number1_entry.get())
    number2 = int(number2_entry.get())
    final_result = number1 + number2
    main_page.iconify()
    showinfo(title="Result",message=f"Total : {final_result}")
    main_page.deiconify()
    number1_entry.delete(first=0,last=len(str(number1)))
    number2_entry.delete(first=0,last=len(str(number2)))
    
    result_file = open("Result.txt","w")
    result_file.write(f"{number1} + {number2} = {final_result}")
    result_file.close()

settings = {
    "ents":{
        "bg" : "#d9ed92" ,
        "fg" : "#184e77" ,
        "font" : ("Space Mono",16) ,
        "relief" : "sunken" ,
        "border" : 20 ,
        "justify" : "center"
    },
    "lbls":{
        "bg" : "#d9ed92" ,
        "fg" : "#184e77" ,
        "font" : ("Space Mono",16) ,
        "relief" : "ridge" ,
        "border" : 25 
    },
    "btns":{
        "bg" : "#168aad" ,
        "fg" : "#ffffff" ,
        "font" : ("Space Mono",16) ,
        "relief" : "raised" ,
        "border" : 25 
    }
}

main_page = Tk()
main_page.title(string="Calculator")
main_page.resizable(0,0)
main_page.config(bg="#1e6091")

total_label = Label(master=main_page,text="Waiting...",cnf=settings["lbls"])

number1_entry = Entry(master=main_page,cnf=settings["ents"])
number2_entry = Entry(master=main_page,cnf=settings["ents"])

confirm_button = Button(master=main_page,text="Press to show!",cnf=settings["btns"],command=calculate)

total_label.grid(row=0,column=0,columnspan=2,sticky="nsew",padx=20,pady=20)
number1_entry.grid(row=1,column=0,sticky="nsew",padx=20,pady=20)
number2_entry.grid(row=1,column=1,sticky="nsew",padx=20,pady=20)
confirm_button.grid(row=2,column=0,columnspan=2,sticky="nsew",padx=20,pady=20)

main_page.mainloop()