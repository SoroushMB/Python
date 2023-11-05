class Pokemon:
    
    """This program will use to create Pokemon Go video game characters!
    Type:
    Bug,Dark,Dragon,Electric,Fairy,Fighting"""
    
    def __init__(self,name:str,Type:str,health:int) -> str:
        self.name = name
        self.Type = Type
        self.health = health
        
    def attack(self):
        print("Attacking!-10 HP")
        
    def dodge(self):
        print("Dodging from attack")
        
    def evolve(self):
        print("Evolving to rival!")


