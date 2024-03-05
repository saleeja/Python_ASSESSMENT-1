"""19.Write program for building restaurant menu using class in Python."""

import time

class Burger:
    AVAILABLE_CUSTOMIZATIONS = {"Cheese": 20, 
                                "Lettuce": 15, 
                                "Mayonnaise": 20, 
                                "Plain Bun.": 15.00,
                                "Whole Wheat Bun.": 20.00,
                                "Sesame Seed Bun":30.00,
                                "Beef Patty": 100.50,
                                "Chicken Patty": 90.00,
                                "Tomato": 4.75,
                                "Pickles": 6.50,
                                "Onions": 3.75,}

    def __init__(self, name, description, price, customizations=None):
        self.name = name
        self.description = description
        self.price = price
        self.customizations = customizations if customizations is not None else []

    def add_customization(self, customization):
        if customization in self.AVAILABLE_CUSTOMIZATIONS:
            self.customizations.append(customization)
        else:
            print(f"Error: '{customization}' is not a valid customization.")

    def get_customizations(self):
        return ", ".join(self.customizations)

    def calculate_customization_cost(self):
        return sum(self.AVAILABLE_CUSTOMIZATIONS.get(customization, 0) for customization in self.customizations)

    def display_available_customizations(self):
        print("Available Customizations:")
        for i, customization in enumerate(self.AVAILABLE_CUSTOMIZATIONS, start=1):
            print(f"{i}. {customization} - ₹{self.AVAILABLE_CUSTOMIZATIONS[customization]:.2f}")

    def calculate_total_price(self):
        return self.price + self.calculate_customization_cost()

    def __str__(self):
        return f"{self.name}: {self.description} - ₹{self.calculate_total_price():.2f} (Customizations: {self.get_customizations()})"

class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, burger, quantity=1):
        for _ in range(quantity):
            self.items.append(burger)

    def calculate_total(self):
        return sum(item.calculate_total_price() for item in self.items)

    def display_cart(self):
        print("----- Cart -----")
        for item in self.items:
            print(item)
        total_amount = self.calculate_total()
        print(f"Total Amount: ₹{total_amount:.2f}")
        print("-----------------")
        return total_amount

class BurgerMenu:
    def __init__(self):
        self.burgers = []

    def add_burger(self, burger):
        self.burgers.append(burger)

    def load_menu_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                current_category = None
                current_subcategory = None
                for line in file:
                    line = line.strip()
                    if line.startswith("#"):
                        current_category = line[2:].strip()
                    elif line.startswith("##"):
                        current_subcategory = line[2:].strip()
                    elif line:
                        parts = line.split(',')
                        if len(parts) >= 2:
                            name, description = parts[0], parts[1]
                            price = float(parts[2]) if len(parts) > 2 and parts[2].replace('.', '').isdigit() else 0.0
                            customizations = [] if len(parts) <= 3 else parts[3].split(',')
                            burger = Burger(name, description, price, customizations)
                            self.add_burger(burger)
                            if current_category:
                                burger.category = current_category
                            if current_subcategory:
                                burger.subcategory = current_subcategory
                        else:
                            print(f"Error: Invalid line in menu file - {line}")
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except ValueError as e:
            print(f"Error: {e}")

    def display_menu(self):
        print("----- FOOD MENU -----")
        current_category = None
        for i, burger in enumerate(self.burgers, start=1):
            if burger.category != current_category:
                print(f"\n{burger.category}")
                current_category = burger.category

            print(f"{i}. {burger}")

        print("-----------------")

def create_your_own_burger(prices):
    burger_name = input("Enter the name for your custom burger: ")
    burger = Burger(burger_name, "Your custom burger", 0.0)
    burger.display_available_customizations()
    customization_numbers = input("Enter the numbers of the customizations you want (comma-separated): ").split(',')
    for number in customization_numbers:
        try:
            burger.add_customization(list(burger.AVAILABLE_CUSTOMIZATIONS.keys())[int(number) - 1])
        except (ValueError, IndexError):
            print("Invalid customization number. Skipping...")

    return burger

def main():
    burger_menu = BurgerMenu()
    burger_menu.load_menu_from_file('menu.txt')
    cart = Cart()

    print("Welcome to the Burger Joint!")
    while True:
        print("\n1. Display Menu")
        print("2. Add Burger to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Create Your Own Burger")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            burger_menu.display_menu()
        elif choice == '2':
            try:
                burger_index = int(input("Enter the burger number to add to your cart (0 to finish): "))
                if burger_index == 0:
                    continue

                burger = burger_menu.burgers[burger_index - 1]
                print(f"Do you want any customizations for '{burger.name}'? (yes/no): ")
                customization_choice = input().strip().lower()

                if customization_choice == 'yes':
                    burger.display_available_customizations()
                    customization_numbers = input("Enter the numbers of the customizations you want (comma-separated): ").split(',')
                    for number in customization_numbers:
                        try:
                            burger.add_customization(list(burger.AVAILABLE_CUSTOMIZATIONS.keys())[int(number) - 1])
                        except (ValueError, IndexError):
                            print("Invalid customization number. Skipping...")

                quantity = int(input(f"How many '{burger.name}' do you want to add to the cart? "))
                cart.add_to_cart(burger, quantity)
                print(f"{quantity} '{burger.name}'(s) added to the cart.")

            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid burger number and quantity.")
        elif choice == '3':
            cart.display_cart()
        elif choice == '4':
            total_amount = cart.calculate_total()
            print(f"Total Amount to Pay: ₹{total_amount:.2f}")
            payment_choice = input("Do you want to proceed with the payment? (yes/no): ").strip().lower()

            if payment_choice == 'yes':
                print("Checking out...")
                time.sleep(2)  # Simulating a payment process
                print("Payment successful!")
                print("Your order will be ready in 10 minutes.")
                time.sleep(10)
                print("Order is ready for pickup!")
                break
            else:
                print("Payment canceled. Your items are still in the cart.")
        elif choice == '5':
            user_burger = create_your_own_burger(Burger.AVAILABLE_CUSTOMIZATIONS)
            cart.add_to_cart(user_burger)
            print(f"{user_burger.name}'s Burger is own the way.")
            print(f"{user_burger.name}'s Burger added to the cart.")
        elif choice == '6':
            print("Exiting. Thank you for using our service!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

main()

