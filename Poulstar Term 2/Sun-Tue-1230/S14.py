store_items = {
    "Greek Yogurt": 50_000,
    "Cheese Puff": 18_000,
    "Iceland Yogurt": 78_000,
    "Clear Shampoo": 80_000,
    "Mihan Ice-Cream": 10_000
}
only_items = list(store_items.keys())

final_price = 0
while True:
    for item in only_items:
        print(f"{item}🗿")
    user_basket = input("\nWhat do you want? ").title()
    if user_basket in only_items:
        count_of_items = int(input("How many of those do you want? "))
        final_price += ((store_items[user_basket]) * count_of_items)
    elif user_basket == "No":
        print(f"Your basket total price : ${final_price:,} Toman!")
        break
    else:
        print("You have entered an insufficient value!\nPlease try again!")
print("Have a good day!")

# :) (😁) , :( (😕) , :| (😐)