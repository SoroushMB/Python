user_input = input("camelCase: ")
for letter in user_input:
    if letter.isupper(): #True , False
        user_input = user_input.replace(f"{letter}",f"-{letter.lower()}")
print(f"snake-case: {user_input}")