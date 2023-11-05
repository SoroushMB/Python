# Error Handling , Exceptions
try:    
    user_input = int(input(">> "))
except:
    print("You haven't entered a number!")
else:
    print(f"The user number is {user_input}")