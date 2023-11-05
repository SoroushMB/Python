# 30 : 1 , 2 , 3 , 5 , 6 , 10 , 15 , 30
# 28 : 1 , 2 , 4 , 7 , 14 -> Perfect Number
try:
    number = 28
    if number < 1:
        raise ValueError
except ValueError:
    print("You have entered a wrong number!")
    