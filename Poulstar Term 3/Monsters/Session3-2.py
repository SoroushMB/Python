from tkinter import Tk,Label,Entry,Button
"""
w = write
a = append
r = read
"""
def main():
    first_name = first_name_ent.get()
    last_name = last_name_ent.get()
    age = age_ent.get()

    file = open("UserInfo.txt","a")
    file.write(f"\nFirst name : {first_name}\nLast name : {last_name}\nAge : {age}")
    file.close()
    print("Saved!")

configurations = {
    "lbls" : {
        "bg" : "lightblue",
        "fg" : "black",
        "font" : ("JetBrains Mono",16),
        "relief" : "raised",
        "border" : 20,
    },
    "ents" : {
        "bg" : "lightblue",
        "fg" : "black",
        "font" : ("JetBrains Mono",16),
        "relief" : "raised",
        "border" : 20,
    },
    "btns" : {
        "bg" : "darkblue",
        "fg" : "white",
        "font" : ("JetBrains Mono",20),
        "relief" : "raised",
        "border" : 20,
    }
}
root = Tk()
root.title("Exercise")
root["bg"] = "darkblue"

first_name_lbl = Label(master=root,text="Enter your first name : ",cnf=configurations["lbls"])
last_name_lbl = Label(master=root,text="Enter your last name : ",cnf=configurations["lbls"])
age_lbl = Label(master=root,text="Enter your age : ",cnf=configurations["lbls"])

first_name_ent = Entry(master=root,cnf=configurations["ents"])
last_name_ent = Entry(master=root,cnf=configurations["ents"])
age_ent = Entry(master=root,cnf=configurations["ents"])

confirm_btn = Button(master=root,text="Press to confirm!",cnf=configurations["btns"],command=main)

first_name_lbl.grid(row=0,column=0,sticky="nsew",padx=20,pady=20)
first_name_ent.grid(row=0,column=1,sticky="nsew",padx=20,pady=20)
last_name_lbl.grid(row=1,column=0,sticky="nsew",padx=20,pady=20)

last_name_ent.grid(row=1,column=1,sticky="nsew",padx=20,pady=20)
age_lbl.grid(row=2,column=0,sticky="nsew",padx=20,pady=20)
age_ent.grid(row=2,column=1,sticky="nsew",padx=20,pady=20)

confirm_btn.grid(row=3,column=0,columnspan=2,sticky="nsew",padx=20,pady=20)

root.mainloop()