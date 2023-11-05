final_result = open("username.txt","r")
lines = final_result.readlines() # List -> Soroush
for line in lines:
    if "Soroush" in line:
        print("👍")
final_result.close()
print(lines)
