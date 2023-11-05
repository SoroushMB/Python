UserNumber = int(input(">> "))
Quantifiers = []
ResultOfSum = 0

for Number in range(1,UserNumber):
    if UserNumber % Number == 0:
        Quantifiers.append(Number)     
for Number in Quantifiers:
    ResultOfSum += Number

if ResultOfSum == UserNumber:
    print("Perfect")
elif ResultOfSum > UserNumber:
    print("Abduct")
elif ResultOfSum < UserNumber:
    print("Deficient")