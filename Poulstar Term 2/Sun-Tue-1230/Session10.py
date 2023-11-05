user_input = input("Greeting: ").lower()
if "hello" is user_input:
    print("$0")
elif "h" in user_input[0]:
    print("$20")
else:
    print("$100")