class Car:
    def __init__(self,Model,Engine):
        self.Model = Model
        self.Engine = Engine
        
    def __str__(self):
        return f"{self.Model} has {self.Engine}"
    
Nissan = Car(Model="GTR R34",Engine="VR38")

print(Nissan)