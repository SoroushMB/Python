# Attributes (Methods + Properties)
class Sony_PlayStation_5_type1:
    # Method (Functions in Class!)
    def __init__(self,owner_name,controller_count,headset,VR_headset,region):
        self.owner_name = owner_name
        self.controller_count = controller_count
        self.headset = headset
        self.VR_headset = VR_headset
        self.region = region
    # Property (Variables in Class!)
    color = "White"
    installation_type = ("Disk","Digital Image")
    price = 499
    storage = "825GB"
    APU_Manufacturer = "AMD"
    APU_Architecture_Name = "Zen 2"
    
    def pricing(self):
        if self.controller_count > 1:
            self.controller_price = ((self.controller_count) * 50)-50
        if self.headset > 0:
            self.headset_price = (self.headset) * 70
        if self.VR_headset > 0:
            self.VR_headset_price = (self.VR_headset) * 170
        return self.price + self.controller_price + self.headset_price + self.VR_headset_price


class Sony_PlayStation_5_type2:
    
    def __init__(self,owner_name:str,controller_count:int,headset:int,VR_headset:int,region:int):
        self.owner_name = owner_name
        self.controller_count = controller_count
        self.headset = headset
        self.VR_headset = VR_headset
        self.region = region

    color = "White"
    installation_type = "Digital Image"
    price = 399
    storage = "825GB"
    APU_Manufacturer = "AMD"
    APU_Architecture_Name = "Zen 2"
    
    def pricing(self):
        if self.controller_count > 1:
            self.controller_price = ((self.controller_count) * 50)-50
        if self.headset > 0:
            self.headset_price = (self.headset) * 70
        if self.VR_headset > 0:
            self.VR_headset_price = (self.VR_headset) * 170
        return self.price + self.controller_price + self.headset_price + self.VR_headset_price
    
avesta = Sony_PlayStation_5_type2(owner_name="Avesta Mirsaeidi",controller_count=2,headset=1,VR_headset=2,region=2)
print(avesta.pricing())