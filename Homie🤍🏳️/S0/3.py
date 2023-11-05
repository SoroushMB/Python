"""String Methods : lower() , upper() , capitalize()
title() , replace() , isupper() , islower() , startswith()
endswith() , isdigit() , strip()
"""
name = input("Name : ").capitalize().replace("a","@")
print(f"Hello, {name}")
print(name.endswith(("H","h")))