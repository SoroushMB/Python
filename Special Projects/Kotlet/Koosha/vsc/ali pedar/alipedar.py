from tkinter import Label,LabelFrame,Button,Entry,Spinbox,Tk,Toplevel
from tkinter.ttk import Combobox
from tkinter.messagebox import showinfo,showerror
from time import sleep,strftime
from random import choice,randint,randrange
from os import system
from platform import system as sys
#komak
def terminal_cleaner():
    os_name=sys()
    if os_name == "Windows" :
        system("cls")
    elif os_name == "Linux" or os_name == "Darwin":
        system("clear")
#komak2
def second_page():
    global name_entry,arrival_d_entry,return_d_entry,start_p_cb,destination_cb,nop_sb
    cities_list=["Tehran","Rasht","Mazandaran","Zanjan"]
    
    second_page=Toplevel()
    second_page.title("Buying Ticket")
    second_page.config(bg="#2c4cd2")
    
    first_label_frame=LabelFrame(second_page,text="Flight Inc.",bg="#2c4cd2")
    name_label=Label(first_label_frame,text="Name",bg="#2c4cd2")
    arrival_d_label=Label(first_label_frame,text="Arrival Date",bg="#2c4cd2")
    return_d_label=Label(first_label_frame,text="Return Date",bg="#2c4cd2")
    start_p_label=Label(first_label_frame,text="Start Place",bg="#2c4cd2")
    destination_label=Label(first_label_frame,text="Destination",bg="#2c4cd2")
    nop_label=Label(first_label_frame,text="Number Of people:",bg="#2c4cd2")
    
    second_label_frame=LabelFrame(second_page,text="Flight Info",bg="darkred")
    name_entry=Entry(second_label_frame)
    arrival_d_entry=Entry(second_label_frame)
    return_d_entry=Entry(second_label_frame)
    start_p_cb=Combobox(second_label_frame,values=cities_list,state="readonly")
    destination_cb=Combobox(second_label_frame,values=cities_list,state="readonly")
    nop_sb=Spinbox(second_label_frame,from_=0,to=4,wrap=True,state="readonly")
    
    third_label_frame=LabelFrame(second_page,text="Saving",bg="darkred")
    save_button=Button(third_label_frame,text="save",command=lambda:save_info())
    exit_button=Button(third_label_frame,text="Exit",command=lambda:second_page.destroy())
    
    first_label_frame.grid(column=0,row=0,sticky="news",padx=20,pady=20)
    second_label_frame.grid(column=1,row=0,sticky="news",padx=20,pady=20)
    third_label_frame.grid(column=0,row=1,sticky="news",padx=20,pady=20)
    third_label_frame.columnconfigure(0,weight=2)
    third_label_frame.columnconfigure(1,weight=2)
    
    name_label.grid(column=0,row=0,sticky="news",padx=10,pady=10)
    arrival_d_label.grid(column=0,row=1,sticky="news",padx=10,pady=10)
    return_d_label.grid(column=0,row=2,sticky="news",padx=10,pady=10)
    start_p_label.grid(column=0,row=3,sticky="news",padx=10,pady=10)
    destination_label.grid(column=0,row=4,sticky="news",padx=10,pady=10)
    nop_label.grid(column=0,row=5,sticky="news",padx=10,pady=10)
    
    name_entry.grid(column=0,row=0,sticky="news",padx=10,pady=10)
    arrival_d_entry.grid(column=0,row=1,sticky="news",padx=10,pady=10)
    return_d_entry.grid(column=0,row=2,sticky="news",padx=10,pady=10)
    start_p_cb.grid(column=0,row=3,sticky="news",padx=10,pady=10)
    destination_cb.grid(column=0,row=4,sticky="news",padx=10,pady=10)
    nop_sb.grid(column=0,row=5,sticky="news",padx=10,pady=10)
    
    save_button.grid(column=0,row=0,sticky="news")
    exit_button.grid(column=1,row=0,sticky="news")
    
    second_page.mainloop()
    
def save_info():
    global name,arrival_d,return_d,start_p,destination,nop_sb
    
    time=strftime("%H:%M")
    name=name_entry.get()
    arrival_d=arrival_d_entry.get()
    return_d=return_d_entry.get()
    start_p=start_p_cb.get()
    destination=destination_cb.get()
    nop=nop_sb.get()
    
    profile_file=open("PassengerInfo.txt","a")
    profile_file.write(f"Time:{time}\n")
    profile_file.write(f"""Name:{name}
Arrival Date:{arrival_d}
Return Date:{return_d}
Start Place:{start_p}
Destination:{destination}
Number Of people:{nop}\n""")
    profile_file.write(30*"._.")
    profile_file.write("\n")
    profile_file.close()
    
def save_initial_info():
    ...
    
second_page()
main_page=Tk()
main_page.title("First page")

username_entry=Label()
username_label=Entry()
password_label=Label()
password_entry=Entry()

main_page.mainloop()