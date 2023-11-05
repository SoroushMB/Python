from pymysql import connect

class Database:
    
    def __init__(self,dbname,host,user,pswd):
        self.dbname = dbname
        self.host = host
        self.user = user
        self.pswd = pswd
        
    def connectToDB(self):
        self.database = connect(db=self.dbname,host=self.host,user=self.user,password=self.pswd)
        self.cursor = self.database.cursor()





















































# def connection(ht,usr,pswd,db):
#     try:
#         connect(host=ht,user=usr,password=pswd,db=db)
#     except Exception:
#         print("There is something wrong with the info you have provided to connect to database!")
#     else:
#         print("Connected!")

# if __name__ == "__main__":
#     connection()