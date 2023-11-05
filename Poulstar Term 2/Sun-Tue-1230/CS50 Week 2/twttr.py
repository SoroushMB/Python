user_expression = input("Input: ").strip()
vowels = ("a","e","o","u","i")
for letter in user_expression.lower():
    if letter in vowels:
        user_expression = user_expression.replace(letter,"")
print(f"Output: {user_expression}")