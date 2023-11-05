"""
Object-Oriented Programming -> Human ==> 
                                        In Common :2 Eyes, 2 Hands, 2 Legs
                                        Different :Name, Hair Color, Age
"""
from pymysql import connect


class Connecting:
    def __init__(self, NameDB, UserDB, PassDB, HostDB):
        self.HostDB = HostDB
        self.UserDB = UserDB
        self.PassDB = PassDB
        self.NameDB = NameDB
    
    def connecting(self):
        cnt = connect(host=self.HostDB,user=self.UserDB,password=self.PassDB,db=self.NameDB)
        self.Agent = cnt.cursor()