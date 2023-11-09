# Inheritance
class Gun:
    def __init__(self,FireRate,Range,Accurancy,Mobility):
        self.FireRate = FireRate
        self.Range = Range
        self.Accurancy = Accurancy
        self.Mobility = Mobility
        
    def __str__(self):
        return f"FireRate:{self.FireRate}\nRange:{self.Range}\nAccurancy:{self.Accurancy}\nMobility:{self.Mobility}"
    
    def shooting(self,Trigger):
        self.Trigger = Trigger
        return f"Trigger kind : {self.Trigger}"
    
class Assualt(Gun):
    def size():
        ...
class AKSeries(Assualt):
    ...
    
FirstGun = Assualt(FireRate=10,Range=10,Accurancy=10,Mobility=10)
print(FirstGun.shooting(Trigger="Auto"))