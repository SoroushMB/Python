import re
from urllib.request import urlopen
from tkinter import Tk,Label

def get_ip() -> str:
    source = urlopen("http://checkip.dyndns.com")
    data = str(source.read())
    return re.search(r"\d+\.\d+\.\d+\.\d",data).group()

ip = get_ip()
main_win = Tk()
main_win.title("IP Revealer")

watcher = Label(master=main_win,
                text=f"Your IP Address : {ip}",
                font=("JetBrains Mono",16),
                bg="#0b132b",
                fg="#6fffe9",
                relief="raised",
                border=20,
                height=5).pack()

main_win.mainloop()
