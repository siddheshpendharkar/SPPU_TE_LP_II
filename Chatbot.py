def show_menu():
    menu = {
        '1': 'Pizza - $10',
        '2': 'Burger - $5',
        '3': 'Pasta - $8',
        '4': 'Salad - $4'
    }
    print("Menu:")
    for key, value in menu.items():
        print(f"{key}. {value}")
    return menu

def take_order(menu):
    order = []
    while True:
        choice = input("Enter the number of the item you want to order (or 'done' to finish): ")
        if choice.lower() == 'done':
            break
        if choice in menu:
            quantity = input(f"How many {menu[choice].split(' -')[0]} would you like to order? ")
            if quantity.isdigit() and int(quantity) > 0:
                order.append((menu[choice], int(quantity)))
                print(f"Added {quantity} x {menu[choice]} to your order.")
            else:
                print("Invalid quantity. Please enter a valid number greater than 0.")
        else:
            print("Invalid choice, please try again.")
    return order

def calculate_total(order):
    total = 0
    prices = {'Pizza - $10': 10, 'Burger - $5': 5, 'Pasta - $8': 8, 'Salad - $4': 4}
    for item, quantity in order:
        total += prices[item] * quantity
    return total

def main():
    print("Welcome to our Food Service!")
    while True:
        print("\nOptions:")
        print("1. View Menu")
        print("2. Order Food")
        print("3. Exit")
        choice = input("Please choose an option (1/2/3): ")

        if choice == '1':
            show_menu()
        elif choice == '2':
            menu = show_menu()
            order = take_order(menu)
            if order:
                total = calculate_total(order)
                print("\nYour order:")
                for item, quantity in order:
                    print(f"- {quantity} x {item}")
                print(f"Total: ${total}")
                print("Thank you for your order! Your food will be ready shortly.")
            else:
                print("No items ordered.")
        elif choice == '3':
            print("Thank you for visiting! Goodbye!")
            print("We hope to see you again soon. Have a great day!")
            break
        else:
            print("Invalid choice, please try again.")
          
main()
