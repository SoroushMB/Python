user_agreement = input("Do you agree? \n>> ").title()
if user_agreement.startswith("Y"):
    print("Welcome!")
elif user_agreement.startswith("N"):
    print("Boro birun!")
else:
    print("Hishhhhhhhh!")
# %