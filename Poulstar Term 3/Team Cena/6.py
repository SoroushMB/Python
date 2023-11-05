# 26 -> "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
# Pangram : The quick brown fox jumps over the lazy dog
#-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
# List , For , Input , List Methods , String Methods
Alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
UserSentence = list(input(">> ").upper())
for Letter in UserSentence:
    if Letter in Alphabet:
        Alphabet.remove(Letter)
    if len(Alphabet) == 0:
        print("The sentence is Pangram!")
        break
print("Finished!")