Students = []
with open("Part9.csv") as file:
    for line in file:
        name , birthplace = line.rstrip().split(",")
        Student = {"Name" : name,"Birthplace" : birthplace}
        Students.append(Student)

for i in Students:
    print(f"{i["Name"]} is from {i["Birthplace"]}")