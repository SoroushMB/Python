# Perfect , Abundunt , Deficient
# 48 -> 1,2,3,4,6,8,12,16,24 = 76 => Abundent
# 28 -> 1,2,4,7,14 = 28 => Perfect
# 8 -> 1,2,4 = 7 => Deficient

UserNum = int(input(">> "))
Quantifiers = []
for Quantifier in range(1,UserNum):
    if UserNum % Quantifier == 0:
        Quantifiers.append(Quantifier)

Result = sum(Quantifiers)
if Result == UserNum:
    print("Perfect Number!")
elif Result > UserNum:
    print("Abundent Number!")
else:
    print("Deficient Number!")