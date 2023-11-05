from emoji import emojize

user_input = input("Input : ")
converted = emojize(user_input,language='alias',variant="emoji_type")

print(f"Output : {converted}")