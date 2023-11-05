# -----------Libraries-----------
from tkinter import Label,LabelFrame,Button,Entry,Spinbox,Tk,Toplevel
from tkinter.ttk import Combobox
from tkinter.messagebox import showinfo,showerror
from time import sleep,strftime
from random import choice,randint,randrange
from os import system
from platform import system as sys

first_label_frame_config = {
    "font":("Consolas",18),
    "bg":"#2c4cd2",
    "fg":"white"
}
# -----------Terminal Cleaning-----------
def terminal_cleaner():
    os_name = sys()
    if os_name == "Windows":
        system("cls")
    elif os_name == "Linux" or os_name == "Darwin":
        system("clear")
# -----------Creating The Buying Page-----------
counter = 0
def second_page_creation(btn):
    global counter,second_page
    if btn == "show":
        counter += 1
        if counter < 2:
            global name_entry,arrival_d_entry,return_d_entry,start_p_cb,destination_cb,nop_sb
            main_page.iconify()
            cities_list = ["Tehran","Berlin","Kandahar","Rasht","Toronto","Venice","Madrid","Canary Island","Tokyo","Rome","Kyoto","Los Angeles","New York"]

            second_page = Toplevel()
            second_page.title("Buying Ticket")
            second_page.config(bg="#2c4cd2")
            
            first_label_frame = LabelFrame(second_page, text="Flights Inc.", font=("JetBrains Mono",7), bg="#2c4cd2")
            name_label = Label(first_label_frame, text="Name:", cnf=first_label_frame_config)
            arrival_d_label = Label(first_label_frame, text="Arrival Date:", cnf=first_label_frame_config)
            return_d_label = Label(first_label_frame, text="Return Date:", cnf=first_label_frame_config)
            start_p_label = Label(first_label_frame, text="Start Place:", cnf=first_label_frame_config)
            destination_label = Label(first_label_frame, text="Destination:", cnf=first_label_frame_config)
            nop_label = Label(first_label_frame, text="Number Of People:", cnf=first_label_frame_config)

            second_label_frame = LabelFrame(second_page, text="Flight Info", font=("JetBrains Mono",7), bg="darkred")
            name_entry = Entry(second_label_frame, font=("Consolas",16))
            arrival_d_entry = Entry(second_label_frame, font=("Consolas",16))
            return_d_entry = Entry(second_label_frame, font=("Consolas",16))
            start_p_cb = Combobox(second_label_frame, values=cities_list, font=("JetBrains Mono",16), state="readonly")
            destination_cb = Combobox(second_label_frame, values=cities_list, font=("JetBrains Mono",16), state="readonly")
            nop_sb = Spinbox(second_label_frame, from_=0, to=4, wrap=True, font=("JetBrains Mono",18), state="readonly")

            third_label_frame = LabelFrame(second_page, text="Saving", font=("JetBrains Mono",7), bg="darkred")
            save_button = Button(third_label_frame,text="Save",font=("JetBrains Mono",16),command=lambda:save_info())
            exit_button = Button(third_label_frame,text="Exit",font=("JetBrains Mono",16),command=lambda:killing_second_page())

            first_label_frame.grid(column=0, row=0, sticky="nsew", padx=20, pady=20)
            second_label_frame.grid(column=1, row=0, sticky="nsew", padx=20, pady=20)
            third_label_frame.grid(column=0, row=1, sticky="nsew", padx=20, pady=20, columnspan=2)
            third_label_frame.columnconfigure(0, weight=1)
            third_label_frame.columnconfigure(1, weight=1)

            name_label.pack(anchor="w",padx=10,pady=10)
            arrival_d_label.pack(anchor="w",padx=10,pady=10)
            return_d_label.pack(anchor="w",padx=10,pady=10)
            start_p_label.pack(anchor="w",padx=10,pady=10)
            destination_label.pack(anchor="w",padx=10,pady=10)
            nop_label.pack(anchor="w",padx=10,pady=10)
            
            name_entry.grid(column=0 ,row=0 ,sticky="nsew", padx=10, pady=10)
            arrival_d_entry.grid(column=0 ,row=1 ,sticky="nsew", padx=10, pady=10)
            return_d_entry.grid(column=0 ,row=2 ,sticky="nsew", padx=10, pady=10)
            start_p_cb.grid(column=0 ,row=3 ,sticky="nsew", padx=10, pady=10)
            destination_cb.grid(column=0 ,row=4 ,sticky="nsew", padx=10, pady=10)
            nop_sb.grid(column=0 ,row=5 ,sticky="nsew", padx=10, pady=10)

            save_button.grid(column=0 ,row=0 ,sticky="nsew")
            exit_button.grid(column=1 ,row=0 ,sticky="nsew")
            
            second_page.mainloop()
        else:
            showerror(title="Alert!",message="Already Open!")

def killing_second_page():
    global counter,second_page
    counter = 0
    second_page.destroy()
    main_page.deiconify()

# -----------Saving Files Functions-----------
def save_info():
    global name,arrival_d,return_d,start_p,destination,nop

    time = strftime("%H:%M:%S")
    name = name_entry.get()
    arrival_d = arrival_d_entry.get()
    return_d = return_d_entry.get()
    start_p = start_p_cb.get()
    destination = destination_cb.get()
    nop = nop_sb.get()

    profile_file = open("PassengerInfo.txt","a")
    profile_file.write(f"Time:{time}\n")
    profile_file.write(f"""Name:{name}
Arrival Date:{arrival_d}
Return Date:{return_d}
Start Place:{start_p}
Destination:{destination}
Number Of People:{nop}""")
    profile_file.write(30*".__.")
    profile_file.close()
    showinfo(title="Finished!",message="You have successfully bought your ticket!")
    
def save_initial_info():
    user_info = open("Login.txt","a")
    username = username_entry.get()
    password = password_entry.get()
    user_info.write(30*"._.")
    user_info.write(f"\nUsername:{username}\nPassword:{password}\n")    
    user_info.close()

main_page = Tk()
main_page.title("First Page")

username_label = Label(main_page, text="Username: ", font=("JetBrains Mono",16))
username_entry = Entry(main_page, borderwidth=10,font=("JetBrains Mono",16))
password_label = Label(main_page, text="Password: ", font=("JetBrains Mono",16))
password_entry = Entry(main_page, show="*",borderwidth=10, font=("JetBrains Mono",16))
register_button = Button(main_page, text="Register", font=("JetBrains Mono",16), command=lambda:save_initial_info())
login_button = Button(main_page, text="Login", font=("JetBrains Mono",16), command=lambda:second_page_creation(btn="show"))

username_label.grid(row=0, column=0, sticky="nsew")
username_entry.grid(row=0, column=1, sticky="nsew",columnspan=2)
password_label.grid(row=1, column=0, sticky="nsew")
password_entry.grid(row=1, column=1, sticky="nsew")
login_button.grid(row=3, column=0, sticky="nsew")
register_button.grid(row=3, column=1, sticky="nsew",columnspan=2)

c=1

vpass_button=Button(main_page,text="👁",command=lambda:showpass())
vpass_button.grid(row=1,column=2)


passpower_label=Label(main_page,text="Choose a password")
checkpass_button=Button(main_page,text="check pass")

checkpass_button.grid(row=2,column=2,sticky="news")
checkpass_button.grid(row=3,column=2)

    

def showpass():
    global c
    c+=1
    if c%2==0:
     password_entry.config(show="")
    elif c%2==1:
     password_entry.config(show="*")

main_page.mainloop()
