# file = open("Test.txt","w") # Read,Append,Write
# file.write("Hello, Everybody!")
# file.close()

# with open("Test.txt","w") as file:
#     file.write("Hello, Everybody!")

import json

with open("test.json") as file:
    Library = json.load(file)

print(Library["Good Company"])