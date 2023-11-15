with open("Part9.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(row)
        print(f"{row[0]} is from {row[1]}")