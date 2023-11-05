while True:
    UserExp = input("Please enter anything you want to get evaluated:\n>> ")
    
    LenOfExp = len(UserExp)
    SwapOfExp = UserExp.swapcase()
    
    Counting = input("Counting needed letter: \n>> ")
    Counter = UserExp.count(Counting)
    
    Swapping = input("What word do you want to put in your sentence? \n>> ")
    RemoveNeededWord = input("Which word do you want to get replaced with the previous word? \n>> ")
    SwappedExp = UserExp.replace(RemoveNeededWord,Swapping)
    
    WordsOfExp = UserExp.split(" ")
    
    print(f"""
    Main expression : {UserExp}
    Length of expression : {LenOfExp}
    Counted word : {Counter}
    Swapped expression : {SwappedExp}
    List of words : {WordsOfExp}
    """)
    Decision = input("Do you wish to try again?(Y/N) \n>> ").strip().capitalize()
    if Decision.startswith("N"):
        break

print("Goodbye!")
    