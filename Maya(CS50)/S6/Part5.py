name = input("Name : ")

# file = open("Part3.txt","a")
# file.write(f"{name}\n")
# file.close()

with open("Part3.txt","a") as file:
    file.write(f"{name}\n")
