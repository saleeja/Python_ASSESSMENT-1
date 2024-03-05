"""19.Write program for building restaurant menu using class in Python."""

import time

# Class representing a Burger
class Burger:
    AVAILABLE_CUSTOMIZATIONS = {"Cheese": 20, "Lettuce": 15, "Mayonnaise": 20}

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


# Class representing a Cart
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
        print(f"Total Amount: {total_amount:.2f}")
        print("-----------------")
        return total_amount

# Class representing a BurgerMenu
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
                        current_category = line[1:].strip()
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
        print("----- Burger Menu -----")
        for i, burger in enumerate(self.burgers, start=1):
            print(f"{i}. {burger}")
        print("-----------------------")


def checkout_and_wait(cart):
    total_amount = cart.display_cart()

    proceed_payment = input(f"Do you want to proceed with the payment? (yes/no): ").lower()
    if proceed_payment == 'yes':
        print("Checking out...")
        time.sleep(2)  # Simulating payment processing
        print("Payment successful!")
        print("Your order will be ready in 10 minutes.")
        time.sleep(10)  # Simulating food preparation time
        print("Order is ready for pickup!")
    else:
        print("Payment canceled. Thank you!")

# Main code block
menu_file_path = "menu.txt"  
burger_menu = BurgerMenu()

# Load the menu from a file
try:
    burger_menu.load_menu_from_file(menu_file_path)
except Exception as e:
    print(f"Error loading menu: {e}")
    exit()

# Display the menu
burger_menu.display_menu()

cart = Cart()

# User interaction loop
while True:
    try:
        user_choice = int(input("Enter the number of the burger you want to add to the cart (0 to finish): "))
        if user_choice == 0:
            break
        elif 1 <= user_choice <= len(burger_menu.burgers):
            selected_burger = burger_menu.burgers[user_choice - 1]

            # Customization option
            customization_prompt = input("Do you want any customizations? (yes/no): ").lower()
            if customization_prompt == 'yes':
                selected_burger.display_available_customizations()
                customization_choice = input("Enter the numbers of the customizations you want (comma-separated): ")
                selected_customizations = [list(Burger.AVAILABLE_CUSTOMIZATIONS.keys())[int(choice) - 1] for choice in customization_choice.split(",")]
                for customization in selected_customizations:
                    selected_burger.add_customization(customization)
            else:
                # Quantity option only if customizations are not needed
                quantity = int(input(f"How many '{selected_burger.name}' do you want to add to the cart? "))
                cart.add_to_cart(selected_burger, quantity)
                print(f"{quantity} '{selected_burger.name}'(s) added to the cart.")

                # Ask if the user needs anything else
                anything_else_prompt = input("Do you need anything else? (yes/no): ").lower()
                if anything_else_prompt != 'yes':
                    break  # Exit the loop if the user doesn't need anything else

        else:
            print("Invalid selection. Please enter a valid burger number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Proceed to checkout
checkout_and_wait(cart)
