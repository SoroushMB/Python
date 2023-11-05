# Dictionary
# key : value
cars = {
    "Mercedes-Benz CLS 63 AMG" : 150000,
    "BMW M8 Competition" : 190000
}
ls_cars = list(cars.keys())
for car in ls_cars:
    print(f"{car} : {cars[car]}")

user_car = input("Which car do you want to add?\n>> ")
user_price = int(input("How much is it? \n>> "))

cars.update({user_car : user_price})
cars.pop("BMW M8 Competition")
ls_cars = list(cars.keys())
for car in ls_cars:
    print(f"{car} : {cars[car]}")
