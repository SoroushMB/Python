user_choice = input("Do you want to register or login? \n>> ").lower()
# "a" = append = اضافه کردن,"w" = write = نوشتن , "r" = read = خوندن
if user_choice == "register":
    username = input("Username : ")
    password = input("Password : ")
    user_info = open("UserInfo.txt","r")
    info_list = user_info.readlines()
    counter = 0
    for line in info_list:
        if password in line or username in line:
            counter += 1
    if counter == 2:
        print("You have already registered in our databases!")
    else:
        user_info = open("UserInfo.txt","a")
        user_info.write(f"Username : {username}\nPassword : {password}\n")
        user_info.close()
        print("Your info have been added to our databases!")

elif user_choice == "login":
    username = input("Username : ")
    password = input("Password : ")
    user_info = open("UserInfo.txt","r")


number = 10
print("🍪" * 10)