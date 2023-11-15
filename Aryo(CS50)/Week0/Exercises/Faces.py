def aryo():
    
    bomboclat = input()
        
    monkey = convert(ARYO=bomboclat)

    print(monkey)

def convert(ARYO):

    bomboclat1 = ARYO.replace(":)", '🙂')

    bomboclat2 = bomboclat1.replace(":(", '🙁')

    return bomboclat2

aryo()