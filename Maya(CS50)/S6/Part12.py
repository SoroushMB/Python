# Student = {
# "Name" : "Maya",
# "Birthplace" : "Tehran"
# }
Students = []
with open("Part9.csv") as file:
    for line in file:
        name , birthplace = line.rstrip().split(",")
        Student = {}
        Student["Name"] = name
        Student["Birthplace"] = birthplace
        Students.append(Student)

for i in Students:
    print(f"{i["Name"]} is from {i["Birthplace"]}")