# Read(r(read)) , Write(w(write),a(append))
user_input = input("Enter your name:\n>> ")

if user_input:
    with open("Username.txt","w") as result:
        result.write(f"Username : {user_input}\n")
else:
    print("You haven't wrote anything!")