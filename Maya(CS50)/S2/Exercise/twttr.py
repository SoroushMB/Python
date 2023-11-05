def main():
    vowels = ["a","e","i","o","u"]
    user_input = input("Input: ")
    for letter in user_input.lower():
        if letter in vowels:
            user_input = user_input.replace(letter,"")
    print(f"Output: {user_input}")
main()
# Twitter -> Twttr 