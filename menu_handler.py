#### Group 2, MIS/BAX 304
## Adriana Sun, as242972
## Emma Kate Balog, ekb986
## Luke Montgomery, lam7473
## Mitali Khatri, mk47223

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
    for item in menu:
        category = item[0]
        name = item[1]
        price = item[2]
        
        if category != last_category:
            print(f"\n=== {category} ===")
            last_category = category
    
        print(f"{name}, ${price:.2f}")

## Adding Orders -- Adriana




## Calculating Subtotal, Tax, and Discount -- Emma


## Receipt Generation -- Mishaal


## Menu Handling -- Mitali

def main():
    menu_file = "BAX304FINAL.txt"
    menu = load_menu(menu_file)
    display_menu(menu)


