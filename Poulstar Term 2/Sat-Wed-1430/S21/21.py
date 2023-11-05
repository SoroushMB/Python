username = input("Username : ") # Soroush
# Open , Write/Read , Close
# Write(w) , Read(r) , Append(a)
writing = open("File_Text.txt","w")
writing.write(f"Username : {username}")
writing.close()
print("Writing has been done!")