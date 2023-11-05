# "a" = append , "w" = write , "r" = read
# username = input("Username: ")
info_file = open("UserInfo.txt","r")
# info_file.write("\n")
# info_file.write(30*"*")
# info_file.write(f"\nUsername: {username}\nDear {username}, welcome to our program!\nYou can do anything with it to make your life easier!")
# info_file.write("\n")
# info_file.write(30*"*")
# info_file.close()
lines = info_file.readlines()
for i in lines:
    print(i)
info_file.close()