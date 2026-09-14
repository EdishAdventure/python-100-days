print("Welcome to Pizza diliveries!")
size = input("What size pizza do you want? S, M, or L ")
pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

pizza_price = 0
if size == "S":
    pizza_price += 15
elif size == "M":
    pizza_price += 20
elif size == "L":
    pizza_price += 25
else:
    print("Invalid size selected. Please choose S, M, or L.")
    exit()  # noqa: PLR1722

if pepperoni == "Y":
    if size == "S":
        pizza_price += 2
    else:
        pizza_price += 3
    if extra_cheese == "Y":
        pizza_price += 1
else:
    if extra_cheese == "Y":
        pizza_price += 1

print(f"Your final bill is: ${pizza_price}.")