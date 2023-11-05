# Dictionary - List - Function - String Methods
cars = {
    "Nissan" : "GTR R35 Nismo Edition",
    "Lamborghini" : "Huracan LP-600",
    "Chevrolet" : "Corvette"
}
factor = open("Cars.txt","a")
factor.write(f"Car : {cars['Chevrolet']}")
factor.write(f"\nCar : {cars['Nissan']}")
factor.write(f"\nCar : {cars['Lamborghini']}")
factor.close()