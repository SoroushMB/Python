from pymysql import connect
from tkinter.messagebox import showerror,showinfo

try:
    connect(host="127.0.0.1",user="root",password="root",db="cars_companies")
except:
    showerror(title="Biaaaaaa!👍",message="Moshkel dari!!!!")
else:
    showinfo(title="Biaaaaaa!👍",message="Nokaretam!!!")
    