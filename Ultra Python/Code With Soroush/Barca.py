chances = 0
while chances < 3:
    user_team = input("Your fav team : ")
    if user_team != "Barcelona":
        chances += 1
        print(f"You have {3 - chances} chances to guess right!")
    else:
        print("You are a member of fam!")
        break
if chances == 3:
    print("Your life doesn't worth it!")