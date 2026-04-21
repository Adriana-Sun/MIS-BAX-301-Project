
tax_rate = 0.0825
discount_rate = 0.1

def loadfile(filename):
    with open(filename, 'r') as file:
        items = {}
        for line in file:
            line = line.strip()
            if line == "" or line.startswith("==="):
                continue
            name, price = line.split(",")
            items[name.strip()] = float(price.strip().replace("$", ""))
    return items

menu = loadfile("BAX304FINAL.txt")

order_items = ["Espresso", "Mocha", "Turkey Sandwich"]
order = [menu[item] for item in order_items]

subtotal = sum(order)
discount = subtotal * discount_rate
discounted_total = subtotal - discount
tax = discounted_total * tax_rate
total = discounted_total + tax

print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount: -${discount:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")