with open("Test.txt") as lines:
    file_lines = lines.readlines()
lines_counter = len(file_lines)

for line in range(lines_counter):
    if "Mohammad Ali" in file_lines[line]:
        print(f"I found the word in line {line+1}")