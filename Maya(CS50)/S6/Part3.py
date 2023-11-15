name = input("Name : ")
# Delete -> Writes new things!!!
file = open("Part3.txt","w")
file.write(name)
file.close()