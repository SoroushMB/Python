user_exp = input(">> ")
for letter in user_exp:
    if letter.isupper():    
        user_exp = user_exp.replace(letter,f"_{letter.lower()}")
print(f"Output: {user_exp}")