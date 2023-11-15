# Numbers : int , float , complex
# Iterable : List , String , Tuple , Dictionary , Set , Frozenset , Range
Name = input(">> ")
Letters = int(input(f"""The name you have entered has {len(Name)}!
Which index do you want to see from this name? """))
print(Name[Letters])