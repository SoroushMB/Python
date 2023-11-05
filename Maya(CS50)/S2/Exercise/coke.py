coke = 50
while True:
    print(f"Amount Due: {coke}")
    inserted_coin = int(input("Insert Coin: "))
    if inserted_coin in {25,10,5}:
        coke -= inserted_coin
    if coke <= 0:
        print(f"Change Owed: {abs(coke)}")
        break