# Shop Menu (Item: Price)
menu = {
    "apple": 20,
    "banana": 10,
    "milk": 30,
    "bread": 25,
    "eggs": 50
}

print("🛒 Welcome to Gudu's Mini Shop")
print("Available Items:")
print("-----------------------------")
for item, price in menu.items():
    print(f"{item.capitalize():10} : ₹{price}")
print("-----------------------------")


# Create an empty dictionary to store order details
cart = {}

while True:
    choice = input("Enter item name to buy (or type 'done' to finish): ").lower()
    if choice == "done":
        break
    elif choice in menu:
        qty = int(input(f"Enter quantity of {choice}: "))
        if choice in cart:
            cart[choice] += qty
        else:
            cart[choice] = qty
    else:
        print("Item not found. Please choose from the menu.")



print("\n🧾 Final Bill")
print("-----------------------------")
total = 0
for item, qty in cart.items():
    price = menu[item]
    cost = price * qty
    total += cost
    print(f"{item.capitalize():10} x {qty} = ₹{cost}")
print("-----------------------------")
gst = total * 0.18  # 18% GST
final_amount = total + gst
print(f"Subtotal       : ₹{total}")
print(f"GST (18%)      : ₹{gst:.2f}")
print(f"Total Amount   : ₹{final_amount:.2f}")
print("-----------------------------")
print("🧡 Thank you for shopping at Gudu's Mini Shop!")
