# Auto Gallery : Class
# Buy - Sell - Info
# Text
# Terminal - Tkinter
# Cars : Color👍 , Ownership👍 , License Plate👍 , Engine👍 , Transmission👍 , Optional Things
# Headlights , Interior
from random import choice

class Ford_Raptor_F150:
    """
Engines : ["5.2 V8", "3.5 V6"]
Transmissions : ["10-Speed Auto", "8-Speed Manual"]
Tires : ["LT315/70R17", "37x12.5R 17"]
    """

    def __init__(self, color, ownership):
        self.color = color
        self.ownership = ownership
        license_plate = str(6*(choice(("A", "B", "C"))))
        self.license_plate = license_plate

    def performance_specs(self, engine, transmission, tires):
        try:
            if engine in ["5.2 V8", "3.5 V6"]:
                self.engine = engine
            if transmission in ["10-Speed Auto", "8-Speed Manual"]:
                self.transmission = transmission
            if tires in ["LT315/70R17", "37x12.5R 17"]:
                self.tires = tires
            return (self.engine, self.transmission, self.tires)
        except Exception:
            print("Please select the right options!")



# first_car = Ford_Raptor_F150(color="Red",ownership="Soroush Babaei")
# print(first_car.performance_specs(engine="5.2 V8",transmission="10-Speed Auto",tires="LT315/70R17"))
