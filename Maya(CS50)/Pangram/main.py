def Main():
    UserSentence = input(">> ")
    Result = Validation(Sentence=UserSentence)
    if Result == True:
        print("Your sentence is pangram")
    else:
        print("Your sentence isn't pangram")
        
# The quick brown fox jumps over the lazy dog
def Validation(Sentence:str):
    Alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    Sentence = Sentence.upper()
    Sentence = list(dict.fromkeys(Sentence))
    Sentence = sorted(Sentence)
    try:
        Sentence.remove(" ")
    except ValueError:
        return Sentence==Alphabets
    else:
        return Sentence==Alphabets
        
if __name__ == "__main__":
    Main()