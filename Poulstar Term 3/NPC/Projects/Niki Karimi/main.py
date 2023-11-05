from tkinter import Tk,Label,StringVar,Button,Entry,Checkbutton,PhotoImage,Toplevel,Frame
from tkinter.messagebox import showerror,showinfo
from tkinter.ttk import Notebook, Combobox, Spinbox
from json import dumps,load
import random as r

#CNF
lbl_cnf={"bg":"SkyBlue2","fg":"Black","font":("SpaceMono",13),"relief":"sunken","border":2}
ent_cnf={"bg":"light sky blue","fg":"Black","font":("SpaceMono",13),"relief":"groove","border":2}
btn_cnf={"bg":"SteelBlue2","fg":"Black","font":("SpaceMono",13)}

#NextPage
def second_page():
    global lbl_cnf, username, XOFrame
    root.deiconify()
    app = Toplevel()
    icon_img = PhotoImage(file="smurf.png")
    app.title(string="SmurfGames")
    app.iconphoto(False,icon_img)
    
    Games = Notebook(master=app,width=640,height=960)
    XOFrame = Frame(master=Games)
    RPSFrame = Frame(master=Games)
    Memory = Frame(master=Games)
    
    greeting_lbl1 = Label(master=XOFrame,text=f"Hi {username}!Welcome to SmurfGames!",cnf= lbl_cnf)
    greeting_lbl2 = Label(master=RPSFrame,text=f"Hi {username}!Welcome to SmurfGames!",cnf= lbl_cnf)
    greeting_lbl3 = Label(master=Memory,text=f"Hi {username}!Welcome to SmurfGames!",cnf= lbl_cnf)
            
    Games.add(child=RPSFrame, text="Rock, Paper, Scissor")
    Games.add(child=XOFrame, text="Tic-Tac-Toe")
    Games.add(child=Memory, text="Memory Game")
    Games.pack()

    greeting_lbl1.grid(row=0,column=0,sticky="nsew")
    greeting_lbl2.grid(row=0,column=0,sticky="nsew")
    greeting_lbl3.grid(row=0,column=0,sticky="nsew")
    point()
    board()
    app.mainloop()

def show_pass():
    ack = watcher.get()
    if ack == "off":
        password_ent.config(show="*")
    elif ack == "on":
        password_ent.config(show="")


def registering():  # sourcery skip: move-assign
    global username, password
    username = username_ent.get()
    password = password_ent.get()
    
    length_of_user = len(username)
    length_of_pass = len(password)
    if length_of_pass >= 8:
        if length_of_user >= 3:    
            user_info = {
                "Username" : username,
                "Password" : password
            }
            dumping = dumps(obj=user_info,indent=2)
            with open(f"{username}.json","w") as file:
                file.write(dumping)
            showinfo(title="Successful",message="Registered Successfully!")
        else:
            showerror(title="Alert!!!",message="Your username is too short!")
    else:
        showerror(title="Alert!!!",message="Your password is too weak!")

def login():
    global username, password
    username = username_ent.get()
    password = password_ent.get()
    try:
        with open(f"{username}.json","r") as file:
            example = load(file)

        if username in example["Username"]:
            if password in example["Password"]:
                showinfo(title="Succeed!",message="Access granted!")
                second_page()
            else:
                showerror(title="Alert!",message="Password isn't correct!")
        else:
            showerror(title="Alert!",message="Username not found!")
    except FileNotFoundError:
        showerror(title="Not found!",message="The user hasn't been registered!")

#XOFrame
def point():
    player_one= points[0]
    player_two= points[1]
    point_frame = Frame(XOFrame)
    player1_lbl= Label(master= point_frame, text=f"Player X:{player_one}", cnf= btn_cnf, pady=5)
    player2_lbl= Label(master= point_frame, text=f"Player Y:{player_two}", cnf= btn_cnf, pady=5)
    point_frame.grid(row=0,column=0,pady=5)
    player1_lbl.grid(row=0,column=0)
    player2_lbl.grid(row=0,column=1)


round= "X"
outcome= ["","","","","","","","",""]
points= [0,0]

def click(btn):
    global round, outcome, points
    btn= int(btn)
    if outcome != "":
        if round =="X":
            outcome[btn] = "X"
            buttons[btn].config(bg="Red", fg="White", text="X", state="disabled") 
            round="O"
        else:
            outcome[btn]= "O"
            buttons[btn].config(bg="Green",fg="white", text="O", state="disabled")
            round="X"
    rules()
print(outcome)

def Winner(winner):
    if winner == "X":
        points[0]+=1
        showinfo(title="EndGame",text="Player X Wins!")
    else:
        points[1]+=1
        showinfo(title="EndGame",text="player O wins!")
    reset()

def rules():
    if (outcome[0]==outcome[1]==outcome[2]) and outcome[0] != "":
        Winner(2)
    elif (outcome[3]==outcome[4]==outcome[5]) and outcome[3] != "":
        Winner(3)
    elif (outcome[6]==outcome[7]==outcome[8]) and outcome[8] != "":
        Winner(8)
    elif (outcome[0]==outcome[3]==outcome[6]) and outcome[6] != "":
        Winner(0)
    elif (outcome[1]==outcome[4]==outcome[7]) and outcome[7] != "":
        Winner(1)
    elif (outcome[2]==outcome[5]==outcome[8]) and outcome[5] != "":
        Winner(5)
    elif (outcome[0]==outcome[4]==outcome[8]) and outcome[4] != "":
        Winner(4)
    elif (outcome[2]==outcome[4]==outcome[6]) and outcome[2] != "":
        Winner(6)
    else:
        draw()
    Winner()

def board():
    global buttons
    board_frame = Frame(XOFrame)
    buttons=[]
    counter= 0
    for row in range (0,3):
        for column in range (0,3):
            value= counter
            x=f"{value}"
            buttons.append(value)
            buttons[value]= Button(master= board_frame, command=lambda:click(x))
            buttons[value].config(width=10,height=5,cnf= btn_cnf)
            buttons[value].grid(row=row,column=column)
            counter += 1
    board_frame.grid(row=2,column=0)

def reset():
    outcome= {"","","","","","","","",""}
    round = "X"
    points()
    board()

def draw():
    if "" not in outcome:
        showinfo(title="EndGame",text="The game equalised!")
        reset()

root = Tk()
icon_img = PhotoImage(file="smurf.png")
root.iconphoto(False,icon_img)
root.title(string="SmurfGames")
root.config(bg="SkyBlue")

watcher = StringVar()
username_lbl = Label(master=root, text="Username : ", cnf= lbl_cnf)
password_lbl = Label(master=root, text="Password : ", cnf= lbl_cnf)
username_ent = Entry(master=root, cnf= ent_cnf)
password_ent = Entry(master=root, cnf= ent_cnf, show="*")
login_btn = Button(master=root, text="Login", cnf= btn_cnf,command=login)
regis_btn = Button(master=root, text="Register", cnf= btn_cnf,command=registering)
show_pass_ckb = Checkbutton(master=root, text="Show Password!",variable=watcher,offvalue="off",onvalue="on",command=show_pass, cnf= btn_cnf)

username_lbl.grid(row=0 ,column=0 ,sticky="nsew")
password_lbl.grid(row=1 ,column=0 ,sticky="nsew")
username_ent.grid(row=0 ,column=1 ,sticky="nsew")
password_ent.grid(row=1 ,column=1 ,sticky="nsew")
show_pass_ckb.grid(row=2 ,column=0 ,columnspan=2 ,sticky="nsew")
login_btn.grid(row=3 ,column=0 ,columnspan=2 ,sticky="nsew")
regis_btn.grid(row=4 ,column=0 ,columnspan=2 ,sticky="nsew")
root.mainloop()
