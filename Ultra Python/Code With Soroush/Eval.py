# Evaluation
user_solution = input("""What are the two numbers which 
one of them is half of the other one and also, 
the result of their multiplication is 50 >> """)
# user_solution = "5*10"
# SQL Injection : SQLite - MySQL - PostgreSQL
# Vulnurability 
# Sniffing : Keylogging (Wireshark)
# Software on server
result = eval(user_solution)
if result == 50:
    print("You have answered correctly!")
else:
    print("You have been wrong!")