from pyfiglet import Figlet
from random import choice
from sys import argv,exit

engine = Figlet(width=1000)
# font = choice(engine.getFonts())
try:    
    if len(argv) == 3 and argv[1] == "-f" or argv[1] == "--font":
        engine.setFont(font=argv[2])
        user_text = input(">>> ")
        print(engine.renderText(user_text))
    else:
        exit(f"You haven't entered the right amount of args!\nArgs count : {len(argv)}")
except IndexError:
    print("Too few command-line arguments")
# print(engine.renderText(text="Hello"))