from pymysql import connect 

ht = "127.0.0.1"
usr = "root"
passwd = "root"
db_name = "library"

connect(host=ht,user=usr,password=passwd,db=db_name)
