# Coke : 50 -> 25 , 10 , 5
coke = 50
while coke > 0:
    print(f"Amount Due: {coke}")
    user_payed = int(input("Insert Coin: "))
    if user_payed in {5, 10, 25}:
        coke -= user_payed
print(f"Change Owed: {abs(coke)}")