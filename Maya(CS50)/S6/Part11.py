sentences = []
with open("Part9.csv") as file:
    for line in file:
        name , birthplace = line.rstrip().split(",")
        sentences.append(f"{name} is from {birthplace}")

for sentence in sorted(sentences):
    print(sentence)
