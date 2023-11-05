from tkinter import Tk,Label,Button,Text,Toplevel,END

def final_result():
    temp_money = str(money_txt.get(index1="1.0",index2=END))
    temp_tip = str(tip_txt.get(index1="1.0",index2=END))
    
    money = float(temp_money.replace("$",""))
    tip = float(temp_tip.replace("%",""))/100
    result = tip*money
    
    main_page.iconify()
    secondary_page = Toplevel()
    result_lbl = Label(master=secondary_page,text=f"Leave ${result:.2f}",cnf=configurations["labels"])
    result_lbl.pack()
    secondary_page.mainloop()

configurations = {
    "labels" : {
        "font" : ("Product Sans Medium",16),
        "fg" : "gray5",
        "bg" : "#ff6d00",
        "relief" : "raised",
        "border" : 20,
        "width" : 15
    },
    "texts" : {
        "font" : ("Product Sans Medium",16),
        "fg" : "gray3",
        "bg" : "#ff9e00",
        "relief" : "ridge",
        "border" : 20,
        "width" : 15,
        "height" : 1
    },
    "buttons" : {
        "font" : ("Product Sans Medium",16),
        "fg" : "gray93",
        "bg" : "#3c096c",
        "relief" : "raised",
        "border" : 20,
        "width" : 15,
        "height" : 2,
        "activebackground" : "black",
        "activeforeground" : "white"
    }
}
main_page = Tk()
main_page.title("Tip Calculator")

money_lbl = Label(master=main_page,text="Price : ",cnf=configurations["labels"])
money_txt = Text(master=main_page,cnf=configurations["texts"])
tip_lbl = Label(master=main_page,text="Tip : ",cnf=configurations["labels"])
tip_txt = Text(master=main_page,cnf=configurations["texts"])
answer_btn = Button(master=main_page,text="Press to show!",cnf=configurations["buttons"],command=lambda:final_result())

money_lbl.grid(row=0,column=0,sticky="nsew")
money_txt.grid(row=0,column=1,sticky="nsew")
tip_lbl.grid(row=1,column=0,sticky="nsew")
tip_txt.grid(row=1,column=1,sticky="nsew")
answer_btn.grid(row=2,column=0,columnspan=2,sticky="nsew")
main_page.mainloop()