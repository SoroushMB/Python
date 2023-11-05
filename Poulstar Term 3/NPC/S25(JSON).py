"""
file = open("class.json","w")
file.write(writing_in_json)
file.close()
"""
from json import load

username = input("Enter your username : ")
password = input("Enter your password : ")
with open("Soroush.json") as jasem:
    example = load(jasem)


if username in example["Username"]:
    if password in example["Password"]:
        print("Access granted!")
    else:
        print("Password isn't correct!")
else:
    print("User not found!")