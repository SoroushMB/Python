from random import choice

moves = ["Rock","Paper","Scissors"]
computer_moves = choice(moves)
user_move = input("What do you want to choose?(Rock,Paper,Scissors)\n>>>").title()

if user_move in moves:
    if computer_moves == user_move:
        print("Tie!")
    elif computer_moves == "Rock" and user_move == "Scissors":
        print("Computer wins!")
    elif computer_moves == "Paper" and user_move == "Rock":
        print("Computer wins!")
    elif computer_moves == "Scissors" and user_move == "Paper":
        print("Computer wins!")
    else:
        print("User wins")
else:
    print("You haven't chosen the right option!")