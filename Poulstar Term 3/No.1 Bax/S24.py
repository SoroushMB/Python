name = input("Enter your name : ")
# test_file = open(file="Feshar_nakhor.txt",mode="w")
# test_file.write(f"Name : {name}")
# test_file.close()
with open(file="Feshar_nakhor.txt",mode="w") as test_file:
    test_file.write(f"Name : {name}")
