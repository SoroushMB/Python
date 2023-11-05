Alphabet = list("abcdefghijklmnopqrstuvwxyz")
UserExpression = list(input(">> ").lower())

for Letter in UserExpression:
    if len(Alphabet) > 0:
        if Letter in Alphabet:
            Alphabet = Alphabet.remove(Letter)
    else:
        print("Pangram")
        break