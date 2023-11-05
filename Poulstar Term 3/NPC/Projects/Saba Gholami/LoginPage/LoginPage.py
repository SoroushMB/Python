import tkinter as tk
from tkinter import messagebox
import pymysql as pysql

connection = pysql.connect(host="localhost", user="root", password="root", db="logininfo")

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if username == "" or password == "":
        messagebox.showerror("Error","Username and Password are required")
        return
    
    with connection.cursor() as cursor:
        sql_query = "SELECT * FROM users WHERE username = "