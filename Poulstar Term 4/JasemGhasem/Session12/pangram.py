alphabet = set(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
user_expression = set(list(input(">> ").upper()))
result = len(alphabet - user_expression)
print("Pangram") if result == 0 else print("Not Pangram!")