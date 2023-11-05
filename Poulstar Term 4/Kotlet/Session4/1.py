# Cookie Factory -> Deposit , Withdraw , Show
# init -> Current , Capacity
# Cookie Jar -> 

class Cookie_Jar:
    
    def __init__(self,current,capacity):
        self.current = current
        self.capacity = capacity
    
    def deposit(self,increment:int):
        if increment <= self.capacity - self.current and increment > 0:
            self.current += increment
        else:
            print("The jar doesn't have the capacity you want!")
    
    def withdraw(self):
        ...
    def show(self):
        ...
        
mine = Cookie_Jar()
