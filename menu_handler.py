#### Group 2, MIS/BAX 304
## Adriana Sun, as242972
## Emma Kate Balog, ekb986
## Luke Montgomery, lam7473
## Mitali Khatri, mk47223
## Mishaal Talha, mt38833

menu = []
order = []

## Menu handling/printig -- Luke
def load_menu(filename):
    current_category = ""

    # 'utf-8-sig' to remove any hidden characters at the beginning
    with open(filename, 'r', encoding = 'utf-8-sig') as file:
        for line in file:
            line = line.strip()

            if line == "":
                continue
            
            if line.startswith("==="):
                current_category = line.replace("=", "").strip()

            if "," not in line:
                continue

            name, price = line.split(",")
            item = [current_category, name.strip(), float(price.strip().replace("$", ""))]

            menu.append(item)
    return menu

def display_menu(menu):
    last_category = None 
    count = 0
    for item in menu:
        category = item[0]
        name = item[1]
        price = item[2]
        
        if category != last_category:
            print(f"\n=== {category} ===")
            last_category = category
    
        print(f"{count}: {name}, ${price:.2f}")
        count += 1

## Adding Orders -- Adriana
def add_order(menu):
    # user will choose item from the menu labeled w/ numbers
    
    # choice should correspond with the Menu index
    valid = False
    while(valid == False):
        choice = input("\nInput menu item #: ")
        # create a try-catch statement to prevent letters from being entered
        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input. Please enter a number.")
        else:
            # check if number is on the menu (0 to length-1)
            if (choice < 0 or choice >= len(menu)):
                print(f"Invalid input. Enter a number between 0 and f{len(menu) - 1}")
            else:
                valid = True
    
    # quantity should be a number greater than 0
    valid = False
    while(valid == False):
        quantity = input(f"Quantity of {menu[choice][1]}: ")
        # create a try-catch statement to prevent letters from being entered
        try:
            quantity = int(quantity)
        except ValueError:
            print("Invalid input. Please enter a number.\n")
        else:
            # check if number is valid
            if (quantity < 0):
                print("Invalid input. Enter a number greater than 0.\n")
            else:
                valid = True
    
    # append [item #, quantity]
    order.append([choice, quantity])
    print("[Successfully added order!]")

## Removing Orders -- Adriana
def remove_order(menu):
    # display order numbers so user can choose which one to remove
    display_orders()
    
    # create a Try-Catch statement to prevent users from inputting letters/words
    valid = False
    while(valid == False):
        choice = input("\nOrder number to remove: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input. Please enter a number.")
        else:
            # check if number is on the orders (0 to length-1)
            if (choice < 0 or choice >= len(order)):
                print(f"Invalid input. Enter a number between 0 and {len(order) - 1}")
            else:
                valid = True
    
    del order[choice]
    print(f"[Successfully removed order {choice}!]")

# used in remove_order() to display order numbers
def display_orders():
    print("\n=== ORDERS ===")
    count = 0
    for o in order:
        # print         order #, item name, and quantity
        print(f"Order #{count}: {menu[o[0]][1]}, {o[1]}qty")
        count += 1

## Calculating Subtotal, Tax, and Discount -- Emma
def calculate_pricing(menu):
    tax_rate = 0.0825
    discount_rate = 0.1

    subtotal = 0
    for order_item in order:
        menu_index = order_item[0]
        item_price = menu[menu_index][2]
        quantity = order_item[1]
        subtotal += item_price * quantity

    discount = subtotal * discount_rate
    discounted_total = subtotal - discount
    tax = discounted_total * tax_rate
    total = discounted_total + tax

    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: -${discount:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")


## Receipt Generation -- Mishaal

def generate_receipt(menu):
    if len(order) == 0:
        print("\n[No items in order!]")
        return
    print("\n========== RECEIPT ==========")

    subtotal = 0
    for o in order:
        item_index = o[0]
        quantity = o[1]

        name = menu[item_index][1]
        price = menu[item_index][2]

        line_total = price * quantity
        subtotal += line_total
        print(f"{name} x{quantity} @ ${price:.2f} = ${line_total:.2f}")

    discount = subtotal * 0.10
    discounted_total = subtotal - discount
    tax = discounted_total * 0.0825
    total = discounted_total + tax
    print("-----------------------------")
    print(f"Subtotal:        ${subtotal:.2f}")
    print(f"Discount (10%): -${discount:.2f}")
    print(f"Tax (8.25%):     ${tax:.2f}")
    print(f"Total:           ${total:.2f}")
    print("=============================")

## Menu Handling -- Mitali

def main():
    global menu
    menu_file = "BAX304FINAL.txt"
    menu = load_menu(menu_file)
    display_menu(menu)


