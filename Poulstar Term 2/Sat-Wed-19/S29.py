# email = input(">> ")
# if "@" in email:
#     print("Moshkeli nist")
# else:
#     print("Hast")
# "Hello,Hi" --> 0$ "Hey" --> 20$ "What's up?" --> 100$ "" --> 1000$

greeting = input(">> ")

if greeting == "Hi" or greeting == "Hello":
    print("0$")
elif greeting == "Hey":
    print("20$")
elif greeting == "What's up?":
    print("100$")
elif greeting == "":
    print("1000$")