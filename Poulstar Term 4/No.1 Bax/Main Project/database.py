from pymysql import connect
from tkinter.messagebox import showerror,showinfo


class Database:
    def __init__(self,Host,Pass,User,Data):
        self.Host = Host
        self.Pass = Pass
        self.User = User
        self.Data = Data
    
    def ConnectToDB(self):
        try:
            self.Connected = connect(host=self.Host,password=self.Pass,user=self.User,database=self.Data)
            self.Agent = self.Connected.cursor()
        except:
            showerror(title="Alert!",message="Cannot connect to database!")
        else:
            showinfo(title="Succeed!",message="Connected!")
    
    def SearchInDB(self, IDNumber):
        try:
            Query = f"select * from books where id={IDNumber}"
            self.Agent.execute(Query)
            Result = self.Connected.commit()
            return Result
        except:
            showerror(title="Alert!",message="Cannot connect to database!")
