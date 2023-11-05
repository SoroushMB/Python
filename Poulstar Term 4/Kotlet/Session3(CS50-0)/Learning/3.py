"""
.lower()
.upper()
.islower()
.isupper()
.capitalize()
.title()
.split()
.strip()
.endswith()
.startswith()
.isdigit()
"""
# name = "Amir"
# other = rf"""Hello, Ariyanaz!Good afternoon!
# \nWelcome to our class!{name}"""
# print(other)

# first_name,mid_name,last_name = input(">> ").split(" ",2)
# print(f"Hello, {first_name}")

greeting = "Hello, How you doing!?"
if greeting.endswith("!?") and greeting.startswith("Hello"):
    print("Are you ok??")
else:
    print("Now we are talking!")
    
phonenumber = "09039851230"
print(phonenumber.isdigit())