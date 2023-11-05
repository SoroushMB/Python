from random import randint

while True:
    try:
        user_level = int(input("Level: "))
    except ValueError:
        continue
    if user_level > 1:
        break
    else:
        continue
computer_selected = randint(1,user_level)

while True:        
        user_guess = int(input("Guess: "))
        if user_guess == computer_selected:
            print("Just right!")
            break
        elif user_guess > computer_selected:
            print("Too large!")
        else:
            print("Too small!")
