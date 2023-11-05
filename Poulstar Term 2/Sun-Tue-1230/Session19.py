name = input("Username: ")
fi_hand = open("Test.txt",mode="w")
fi_hand.write(f"Name: {name}")
fi_hand.close()