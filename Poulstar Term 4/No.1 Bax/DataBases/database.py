from pymysql import connect


class Connection:
    def __init__(self, username, password, database, hostname):
        self.username = username
        self.password = password
        self.database = database
        self.hostname = hostname
        
    def connectToDB(self):
        connect(user=self.username,password=self.password,db=self.database,host=self.hostname)
        