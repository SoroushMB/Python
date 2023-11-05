# example_file = open("Test.txt","a")
# example_file.write("Hi Everybody!\nThis is a test text to show you\nhow you can store many lines in a .txt file!")
# example_file.close()

# with open("Test.txt","a") as example_file:
#     example_file.write("Hi Everybody!\nThis is a test text to show you\nhow you can store many lines in a .txt file!")
with open("Test.txt") as example_file:
    lines = example_file.readlines()
for num_line in range(len(lines)):    
    print(f"{num_line+1}:{lines[num_line]}")