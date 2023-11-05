try:  
    num = int(input(">> "))  
    print(num/0)
except ZeroDivisionError:
    print(f"{num/1}")