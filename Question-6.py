"""6.Write a Python function that takes a list of strings as input and returns a 
new list with the strings sorted in descending order of their lengths"""


class DescendingOrder:
    def __init__(self, user_input):
        self.user_input = user_input

    def sort_to_desc(self):
        try:
            input_list = [float(item) for item in self.user_input.split(",")]

            sorted_list = sorted(input_list, reverse=True)

            print("Sorted in descending order:", sorted_list)

        except ValueError:
            print("Error: Enter valid numeric values separated by commas.")

# Get user input for the items separated by commas
user_input = input("Enter the items separated by commas: ")

descending = DescendingOrder(user_input=user_input)

descending.sort_to_desc()

