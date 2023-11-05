# Object Oriented Programming
# Real World!
# Human
# Attribute : Variables(Properties) , Functions(Methods)

class Nissan_GTR_R34:
    
    def __init__(self,color,tuner,owner_name):
        
        self.color = color
        self.tuner = tuner
        self.owner_name = owner_name

    def pricing(self):  # sourcery skip: extract-duplicate-method, switch
        
        if self.tuner == "Nismo":
            self.engine = {"RB26-TwinTurbo-Z Tune Stage 2":2.8}
            self.suspension = "Drift Pack"
            return self.starting_price + 10_000
        
        elif self.tuner == "Normal":
            return self.starting_price
        
        elif self.tuner == "Nagata":
            self.engine = {"V12 Quad-Turbo Stage 3":6.7}
            self.suspension = "Racing Pack"
            return self.starting_price + 60_000

    differential = "AWD"
    transmission = "6-Speed"
    engine = {"RB26-TwinTurbo Stage 1":2.6}
    starting_price = 70_000
    suspension = "Street Pack"


first_product = Nissan_GTR_R34(color="Metallic Blue",tuner="Nagata",owner_name="Soroush Masoum Babaei")
print(first_product.pricing())

# Nissan GTR R34 -> Blue , Matte Black , White , RB26(TwinTurbo) , ...