# Perfect Number
def Main():
    UserNumber = int(input(">> "))
    FirstExample = Identifier(Number=UserNumber)
    if FirstExample > 60:
        print("Abduct Number!")
    elif FirstExample == 60:
        print("Perfect Number!")
    else:
        print("Deficient Number!")
    
def Identifier(Number:int):
    Samples = list(range(1,Number-1))
    Quantifiers = []
    for Sample in Samples:
        if Number%Sample == 0:
            Quantifiers.append(Sample)
    else:
        Result = Summation(Numbers=Quantifiers)
    return Result

def Summation(Numbers:list):
    Counter = 0
    for Number in Numbers:
        Counter += Number
    else:
        return Counter
    
if __name__ == "__main__":
    Main()