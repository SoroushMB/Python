from tkinter import Label,LabelFrame,Button,Spinbox,Tk
from tkinter.ttk import Combobox
from time import strftime
from os import system
from platform import system as sys
# -----------Terminal Cleaning-----------
def terminal_cleaner():
    os_name = sys()
    if os_name == "Windows":
        system("cls")
    elif os_name in ["Linux", "Darwin"]:
        system("clear")

first_label_frame_config = {
    "font":("Consolas",18),
    "bg":"#2c4cd2",
    "fg":"white"
}

main_page = Tk()
main_page.title("komak")

cars=["nissan","toyota"]
models=[]
engines=[]

first_frame=LabelFrame(main_page, bg="grey")
second_frame=LabelFrame(main_page, bg="dark grey",text="model & engine:")
third_frame=LabelFrame(main_page, bg="grey",text="cost:",fg="white")
forth_frame=LabelFrame(main_page, bg="dark grey")

#########################
first_frame.grid(row=0,column=0,sticky="news",padx=10,pady=10)

cars_cb=Combobox(first_frame,values=cars,state="readonly",width="28")
cars_cb.grid(row=0,column=0,padx=10,pady=10)

cars_btn=Button(first_frame,text="next",command=lambda:model(),width=5)
cars_btn.grid(row=0,column=1,padx=5,pady=5)

##########################
second_frame.grid(row=1,column=0,sticky="news",padx=10,pady=10)

model_sb=Spinbox(second_frame,state="readonly",wrap=True,textvariable="model",width="29")
model_sb.grid(row=0,column=0,padx=10,pady=1)

engine_sb=Spinbox(second_frame,state="readonly",wrap=True,textvariable="engine",width="29")
engine_sb.grid(row=1,column=0,padx=10,pady=1)

cars_btn=Button(second_frame,text="engine",command=lambda:engine(),height=1,width=5)
res_btn=Button(second_frame,text="submit",command=lambda:recipt(),height=1,width=5)

cars_btn.grid(row=0,column=1,padx=5,pady=5)
res_btn.grid(row=1,column=1,padx=5,pady=5)

############################
third_frame.grid(row=2,column=0,sticky="news",padx=10,pady=10)

recipt_lbl=Label(third_frame,width=36,height=3)
recipt_lbl.pack(anchor="center",padx=4,pady=4)

###########################
forth_frame.grid(row=3,column=0,sticky="news",padx=10,pady=10)

save_btn=Button(forth_frame,text="save",width=17,command=lambda:save())
exit_btn=Button(forth_frame,text="exit",width=17,command=lambda:destroy())
save_btn.grid(row=0,column=0,padx=3,pady=3,sticky="news")
exit_btn.grid(row=0,column=1,padx=3,pady=3,sticky="news")

def model():
   global models,engines
   c=cars_cb.get()
   if c=="nissan":
     mls)
     recipt_lbl.config(text="")
     engine_sb.config(state="disabled")    odels=["gtr r34","gtr r35"]
     model_sb.config(state="readonly",values=mode
   elif c=="toyota":
     models=["supra mk4","supra mk5"]
     model_sb.config(state="readonly",values=models)
     recipt_lbl.config(text="")
     engine_sb.config(state="disabled")

def engine():
    f=model_sb.get()
    if f=="gtr r34":
        engines=["RB26DETT","RB26DETT twin turbo"]
        recipt_lbl.config(text="")
        engine_sb.config(state="readonly",values=engines)
    elif f=="gtr r35":
        engines=["VR38DETT","VR38DETT twin turbo"]
        recipt_lbl.config(text="")
        engine_sb.config(state="readonly",values=engines) 
    elif f=="supra mk4":
        engines=["2jz","2jz gte"]
        recipt_lbl.config(text="")
        engine_sb.config(state="readonly",values=engines)
    elif f=="supra mk5":
        engines=["MA55","MA46"]
        recipt_lbl.config(text="")
        engine_sb.config(state="readonly",values=engines)
def recipt():
    a=engine_sb.get()
    #r34
    if a=="RB26DETT":
        recipt_lbl.config(text="35,000$")
    elif a=="RB26DETT twin turbo":
        recipt_lbl.config(text="43,000$")
    #r35
    elif a=="VR38DETT":
        recipt_lbl.config(text="67,000$")
    elif a=="VR38DETT twin turbo":
        recipt_lbl.config(text="82,000$")
    #supra mk4
    elif a=="2jz":
        recipt_lbl.config(text="25,000$")
    elif a=="2jz gte":
        recipt_lbl.config(text="38,000$")
    #supra mk5
    elif a=="MA55":
        recipt_lbl.config(text="65,000$")
    elif a=="MA46":
        recipt_lbl.config(text="74,000$")
def save():
    time = strftime("%H:%M:%S")
    user_info = open("recipt.txt","a")
    brand = cars_cb.get()
    model = model_sb.get()
    engine = engine_sb.get()
    cost = recipt_lbl['text']
    user_info.write(30*"._.")
    user_info.write("\n")
    user_info.write(f"Time:{time}\n")
    user_info.write(f"""Brand:{brand}
Model:{model}
Engine model:{engine}
Price:{cost}\n""")
    user_info.close()  
def destroy():
    main_page.destroy()

main_page.mainloop()