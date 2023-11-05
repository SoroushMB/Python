# Coke Price : 50
# Coins : 5,10,25
# 0 -> 10 -> 35 -> 45 -> 50
coke_price = 50
user_paid = 0
while True:
    print(f"Amount Due: {coke_price - user_paid}")
    user_coin = int(input("Insert Coin: "))
    if user_coin in {5,10,25}:
        user_paid += user_coin
        if user_paid >= coke_price:
            print(f"Change Owed: {user_paid - coke_price}")
            break
        else:
            continue
    else:
        continue
    