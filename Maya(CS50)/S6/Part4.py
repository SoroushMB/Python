name = input("Name : ")

file = open("Part3.txt","a")
file.write(f"{name}\t")
file.close()