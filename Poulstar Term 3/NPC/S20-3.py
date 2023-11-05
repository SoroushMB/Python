wanted_name = input("The name you want to find: ").title()
with open("Username.txt","r") as final_result:
    lines = final_result.readlines()
for name in lines:
    if wanted_name in name:
        print("I found it!🗿")
    else:
        print("I didn't found it!😕")
