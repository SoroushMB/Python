# database.py

from pymysql import connect

class Database:
    def __init__(self, Database, Host, Name, Password):
        self.Database = Database
        self.Host = Host
        self.Name = Name
        self.Password = Password
        
    def Connecting(self):
        self.ConnectingToDB = connect(host=self.Host ,user=self.Name ,password=self.Password ,database=self.Database)
        self.Agent = self.ConnectingToDB.cursor()