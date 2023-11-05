user_agreement = input(f"Are you sure you want to buy it(y/n)?\n>> ").lower()
if user_agreement.startswith("ye") or user_agreement.endswith("es"):
    print("Congrats your book have added to your basket!")
elif user_agreement.startswith("n"):
    print("Alright, the book has been deleted from your basket.")
else:
    print("Error!You have entered a wrong word!")