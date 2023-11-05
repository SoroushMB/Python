writing = open("File_Text.txt","r")
# for _ in range(8):    
#     print(writing.readline())#1
# while True:
#     print(writing.readlines())
file_lines = writing.readlines() # A List from all your lines in the specific file!
print(len(file_lines))
writing.close()