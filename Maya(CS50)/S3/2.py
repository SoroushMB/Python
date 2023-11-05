# Loops
while True:
    try:    
        user_input = int(input(">> "))
    except ValueError:
        print("You haven't entered a number!")
    else:
        break
print(f"Number is {user_input}")
