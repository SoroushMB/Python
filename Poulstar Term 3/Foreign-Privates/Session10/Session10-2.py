name = input("Your name : ")
with open("Guys.txt","a") as my_file:
    my_file.write("Guys : Artin , Aryo")
    my_file.write(f"Username : {name}")
# my_file = open("Guys.txt","a")
# my_file.write("Guys : Artin , Aryo")
# my_file.write(f"Username : {name}")
# my_file.close()