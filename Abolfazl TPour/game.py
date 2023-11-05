import random
while True:
    try:
        selected_level = int(input("Level: "))
        if selected_level > 0:
            break
        else:
            continue
    except ValueError:
        continue
    
computer_selected_number = random.randint(1,selected_level)
while True:
    try:
        user_guess = int(input("Guess: "))
        if computer_selected_number > user_guess:
            print("Too Small!")
        elif computer_selected_number < user_guess:
            print("Too Large!")
        else:
            print("Just Right!")
            break
    except ValueError:
        continue