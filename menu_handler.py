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
            if line == "" or line.startswith("==="):
                continue

            name, price = line.split(",")
            item = [name.strip(), float(price.strip().replace("$", ""))]

            menu.append(item)
    return menu

def display_menu(menu):
    for item in menu:
        print(f"{item[0]}, ${item[1]:.2f}")

## Adding Orders -- Adriana




## Calculating Subtotal, Tax, and Discount -- Emma


## Receipt Generation -- Mishaal


## Menu Handling -- Mitali

def main():
    menu_file = "BAX304FINAL.txt"
    menu = load_menu(menu_file)
    display_menu(menu)


