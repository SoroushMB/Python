coke = 50
while coke > 0:
    print(f"Amount Due: {coke}")
    user_coin = int(input("Insert Coin: "))
    if user_coin in {25,10,5}:
        coke -= user_coin
print(f"Change Owed: {coke}")