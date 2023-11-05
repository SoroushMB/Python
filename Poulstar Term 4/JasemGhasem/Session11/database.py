from pymysql import connect
from tkinter.messagebox import showinfo,showerror

class Database:
    def __init__(self, user, pswd, host, dbname):
        self.user = user
        self.pswd = pswd
        self.host = host
        self.dbname = dbname
        
    def connectToDB(self):
        try:
            self.db = connect(user=self.user,password=self.pswd,host=self.host,db=self.dbname)
            self.agent = self.db.cursor()
        except:
            showerror(title="Alert!",message="Not connected!")
        else:
            showinfo(title="Success!",message="Connected!")