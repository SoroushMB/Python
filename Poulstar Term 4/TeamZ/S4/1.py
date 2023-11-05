class Cookie_Factory:
    
    def __init__(self,current:int=8,capacity:int=12):
        self.capacity = capacity
        self.current = current
        
    def deposit(self,increment):
        if increment < (self.capacity - self.current):
            self.current += increment
        
    def withdraw(self):
        ...
        
    def show(self,mode:int):
        if mode == "Current":
            print(self.current * "🍪")
        elif mode == "Capacity":
            print(self.capacity * "🍪")
#Annotation

first_factory = Cookie_Factory(capacity=15)
print(first_factory.capacity)