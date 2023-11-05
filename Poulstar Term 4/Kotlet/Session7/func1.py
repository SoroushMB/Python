def Main():
    Info = GetInfo()
    Name = Info[0]
    print(f"{Name} From")
    
def GetInfo():
    return [input(">> "),input(">> ")]

Main()