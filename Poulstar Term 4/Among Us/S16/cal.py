from pymysql import connect

class calc:
    def __init__(self,number1:int,number2:int):
        self.number1 = number1
        self.number2 = number2
    
    def result(self):
        mul_nums = self.number1 * self.number2
        sum_nums = self.number1 + self.number2
        min_nums = self.number1 - self.number2
        dev_nums = self.number1 / self.number2
        
        return (mul_nums,sum_nums,min_nums,dev_nums)

first = calc(number1=10,number2=20)
nums = first.result()

database = connect(host="127.0.0.1",user="root",password="root",db=)