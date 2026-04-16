#### Group 2, MIS/BAX 304
## Adriana Sun, as242972
## Emma Kate Balog, ekb986
## Luke Montgomery, lam7473
## Mitali Khatri, mk47223


def load_menu(filename):
    menu = []

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