#### Group 2, MIS/BAX 304
## Adriana Sun, as242972
## Emma Kate Balog, ekb986
## Luke Montgomery, lam7473
## Mitali Khatri, mk47223
menu = []
order = []

def load_menu(filename):
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line == "" or line.startswith("===") or "," not in line:
                continue

            name, price = line.split(",")
            item = [name.strip(), float(price.strip().replace("$", ""))]

            menu.append(item)
    return menu

def display_menu(menu):
    for item in menu:
        print(f"{item[0]}, ${item[1]:.2f}")

## Adding Orders -- Adriana
def add_order(menu):
    display_menu(menu)

    # user will choose item from the menu labeled w/ numbers
    # choice should correspond with the Menu index
    choice = int(input("Menu item #: "))
    while (choice < 0 or choice >= len(menu)):
        choice = int(input("Invalid input! Re-enter menu item #: "))
    
    quantity = int(input(f"Quantity of {menu[choice]} (must be > 0): "))
    while (quantity < 0):
        quantity = int(input(f"Invalid input! Re-enter quantity of {menu[choice]} (must be > 0): "))
    
    # append [item #, quantity]
    order.append([choice, quantity])
    print("Successfully added order!")

## Removing Orders -- Adriana
def remove_order(menu):
    # display the orders so user can choose which one to remove
    count = 0
    for o in order:
        # print order #, item name, and quantity
        print(f"Order #{count}: {menu[o[0]][0]}, {o[1]}")
        count += 1
    
    choice = int(input("Order #: "))
    while (choice < 0 or choice >= len(order)):
        choice = int(input("Invalid input! Re-enter order #: "))
    
    del order[choice]
    print(f"Successfully removed order {choice}!")

# testing code (ignore)
# load_menu("BAX304FINAL.txt")
# display_menu(menu)
# add_order(menu)
# remove_order(menu)
## Calculating Subtotal, Tax, and Discount -- Emma


## Receipt Generation -- Mishaal
