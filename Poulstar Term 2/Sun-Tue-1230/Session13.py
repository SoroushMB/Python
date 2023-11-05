# Dictionary : key : value
supermarket_items = {
    # (key : value) -> item
    "Shampoo" : 80000,
    "Chips" : 190000,
    "Cheese-Puff" : 18000,
    "Coca-Cola" : 17000
}

items = list(supermarket_items.keys())

for vasile in items:
    print(vasile)
    
user_input = input("Items you want : ").capitalize()
print(f"Price : ${supermarket_items[user_input]}")