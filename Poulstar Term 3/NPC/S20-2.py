with open("Username.txt","r") as final_result:
    lines = final_result.readlines()
for name in lines:
    if "parsa" in name:
        print("I found it!🗿")
    else:
        print("I didn't found it!😕")
