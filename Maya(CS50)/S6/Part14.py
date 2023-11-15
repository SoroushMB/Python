Students = []
with open("Part9.csv") as file:
    for line in file:
        name , birthplace = line.rstrip().split(",")
        Students.append({"Name" : name,"Birthplace" : birthplace})

for i in Students:
    print(f"{i["Name"]} is from {i["Birthplace"]}")
    