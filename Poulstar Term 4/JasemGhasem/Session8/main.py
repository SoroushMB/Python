from pymysql import connect as cnt
import pymysql
from tkinter.messagebox import showerror

try:
    cnt(host="127.0.0.1",user="root",password="root",db="libarary")
except pymysql.err.OperationalError:
    showerror(message="The name of the db isn't correct!")