# with open("Part9.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is from {row[1]}")
with open("Part9.csv") as file:
    for line in file:
        name , birthplace = line.rstrip().split(",")
        print(f"{name} is from {birthplace}")