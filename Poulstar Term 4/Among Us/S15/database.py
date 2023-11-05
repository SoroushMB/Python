from pymysql import connect
from tkinter.messagebox import showerror,showinfo

class Database:
    
    def __init__(self,dbname,host,user,pswd):
        self.dbname = dbname
        self.host = host
        self.user = user
        self.pswd = pswd
        
    def connectToDB(self):
        try:
            self.database = connect(db=self.dbname,host=self.host,user=self.user,password=self.pswd)
            self.agent = self.database.cursor()
        except:
            showerror(title="Alert!",message="Not connected!")
        else:
            showinfo(title="Alert!",message="Connected!")
        