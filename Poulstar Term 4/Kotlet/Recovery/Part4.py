try:    
    Number = int(input(">> "))
    print(Number + Number)
except ValueError:
    print("Adam bash!Dorost vared kon!")
except EOFError:
    print("Dadash nemikhay chizi bezari?\nMikhai man bezarmmmmmm??")
except:
    print()
else:
    print("Damet garm!Titab talaee!")