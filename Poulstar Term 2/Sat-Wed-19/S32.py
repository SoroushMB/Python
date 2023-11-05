coke_price = 50
user_payment = 0
while True:
    user_coin = int(input("Insert your coin(25,10,5): "))
    if user_coin == 25 or user_coin == 10 or user_coin == 5:
        user_payment += user_coin
        if user_payment >= coke_price:
            print(f"Here is your coke bottle!\nAlso,here is your change:{user_payment - coke_price}")
            break
        else:
            print(f"Amount Due: {coke_price - user_payment}")
            continue
    else:
        print(f"The given coin isn't acceptable!\nAmount Due: {coke_price - user_payment}")
        continue