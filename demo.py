# def load_menu_from_file(filename):
#     menu_items = []

#     try:
#         with open(filename, 'r') as file:
#             for line in file:
#                 line = line.strip()
#                 if line.startswith("# Category:"):
#                     category = line.split(":")[1].strip()
#                 elif line.startswith("## Subcategory:"):
#                     subcategory = line.split(":")[1].strip()
#                 elif line:
#                     item_info = line.split(',')
#                     if len(item_info) == 3:
#                         item_name, item_description, item_price = map(str.strip, item_info)
#                         item = {
#                             'category': category,
#                             'subcategory': subcategory,
#                             'name': item_name,
#                             'description': item_description,
#                             'price': float(item_price)
#                         }
#                         menu_items.append(item)

#     except FileNotFoundError:
#         print(f"File {filename} not found.")

#     return menu_items

# def display_menu(menu_items):
#     print("--------------Burger Time------------------\n")
   
#     current_category = None
#     current_subcategory = None

#     for item in menu_items:
#         if item['category'] != current_category:
#             current_category = item['category']
#             print(f"\n{current_category}{'-' * (30 - len(current_category))}")

#         if item['subcategory'] != current_subcategory:
#             current_subcategory = item['subcategory']
#             print(f"{current_subcategory}{'-' * (30 - len(current_subcategory))}")

#         print(f"{item['name']}: {item['description']} - ${item['price']:.2f}")


# menu_data = load_menu_from_file("menu.txt")
# display_menu(menu_data)





import ast

class RestaurantMenu:
    def __init__(self, menu_file):
        self.menu = self.load_menu(menu_file)
        self.cart = []

    def load_menu(self, file_name):
        menu = {}
        with open(file_name, 'r') as file:
            content = file.read()
            sections = content.split('# Category:')
            for section in sections[1:]:
                lines = section.strip().split('\n')
                category = lines[0].strip()
                items = {}
                for item in lines[1:]:
                    subcategory, *details = item.split('## Subcategory:')
                    subcategory = subcategory.strip()
                    if len(details) >= 3:
                        name = details[0].strip()
                        description = details[1].strip()
                        price = float(details[2].replace('₹', '').strip())
                        items[name] = {'description': description, 'price': price}
                    else:
                        print(f"Invalid entry in menu for '{subcategory}'. Skipping this item.")
                menu[category] = items
        return menu


    def display_menu(self):
        for category, items in self.menu.items():
            print(f"\n{category}")
            for subcategory, details in items.items():
                print(f"{subcategory}: {details['description']} - ₹{details['price']:.2f}")

    def add_to_cart(self, category, item_name):
        if category in self.menu and item_name in self.menu[category]:
            self.cart.append({'category': category, 'item_name': item_name, 'price': self.menu[category][item_name]['price']})
            print(f"{item_name} added to the cart.")
        else:
            print("Invalid category or item name. Please check the menu.")

    def view_cart(self):
        if not self.cart:
            print("Cart is empty.")
        else:
            print("\nYour Cart:")
            for item in self.cart:
                print(f"{item['item_name']} - ₹{item['price']:.2f}")

    def place_order(self):
        total_price = sum(item['price'] for item in self.cart)
        print(f"\nTotal Price: ₹{total_price:.2f}")
        table_number = input("Enter the table number for the order: ")
        print(f"Order placed for Table {table_number}. Enjoy your meal!")

if __name__ == "__main__":
    menu_file = "menu.txt"
    restaurant = RestaurantMenu(menu_file)

    while True:
        print("\n1. Display Menu")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Place Order")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            restaurant.display_menu()
        elif choice == '2':
            category = input("Enter the category: ")
            item_name = input("Enter the item name: ")
            restaurant.add_to_cart(category, item_name)
        elif choice == '3':
            restaurant.view_cart()
        elif choice == '4':
            restaurant.place_order()
            break
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")
