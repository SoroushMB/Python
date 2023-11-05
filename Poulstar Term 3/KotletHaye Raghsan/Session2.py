# firstFileName = 0 : camelCase
# FirstFileName = 0 : PascalCase
# iFirstFileName = 0 : HungarianNotation
# first_file_name = 0 : snake_case
# first-file-name = 0 : kebab_case

def Naming():
    first_name = input(">> ")
    last_name = input(">> ")
    return f"{first_name} {last_name}"
# print() # Built-In
# Naming() # User-Defined

if __name__ == "__main__":
    Naming()