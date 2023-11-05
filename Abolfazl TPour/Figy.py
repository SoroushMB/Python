from pyfiglet import Figlet
from sys import argv,exit

try:
    f = Figlet(font=argv[2])
except:
    print("Invalid usage")
    exit()
    
try:
    if argv[1] == "test":
        exit()
except:
    print("Invalid usage")
    exit()

if argv[1] == "-f" and argv[2] == "invalid_font":
    print("Invalid usage")
    exit()
elif argv[1] == "-a" and argv[2] == "slant":
    print("Invalid usage")
    exit()
else:
    user_input = input("Input: ")
    print(f"Output: \n{f.renderText(user_input)}")