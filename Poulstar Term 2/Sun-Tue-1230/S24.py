# Input ( Username , Password ), Save(txt) , Lookup(txt) if exist show error else ...
# Login , Register
from sys import exit

def login():
    lines = []
    counter = 0
    username = input("Username: ")
    password = input("Password: ")
    
    try:
        with open("Info.txt") as the_file:
            lines = the_file.readlines()
    except FileNotFoundError:
        open("Info.txt","x")
    
    for line in lines:
        if username in line:
            counter += 1
            break
    else:
        print("We haven't found your username in our databases!")
    
    for line in lines:
        if password in line:
            counter += 1
            break
    else:
        print("We haven't found your password in our databases!")
    
    if counter == 2:
        print("Access Granted!")
    else:
        print("Access Denied!")

def register():
    counter = 0
    username = input("Username: ")
    password = input("Password: ")
    
    with open("Info.txt") as the_file:
        lines = the_file.readlines()
    
    for line in lines:
        if username in line:
            counter += 1
            break
    
    if counter == 1:
        print("Your info already exists in our databases!")
    else:
        with open("Info.txt","a") as the_file:
            the_file.write(f"\nUsername: {username}\nPassword: {password}")
            the_file.write(40*"-")


while True:
    user_selection = input("Hi, Would you like to 'Register' or 'Login'?\n<<If you like you can exit the program by typing 'exit'>>\n>> ").lower()

    if user_selection == "login":
        login()
        break
    elif user_selection == "register":
        register()
        break
    elif user_selection == "exit":
        exit("Have a nice day!Good bye!")
    else:
        continue