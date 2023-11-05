coke_price = 50
paid = 0
coins = [5,10,25]
while coke_price > paid:
    print(f"Amount Due : {coke_price - paid}")
    user_pay = int(input("Insert Coin : "))
    if user_pay in coins:
        paid += user_pay
print(f"Change Owed : {paid - coke_price}")