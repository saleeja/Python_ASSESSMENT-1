"""7. Write a function that takes a list of numbers as input and returns the 
second-largest number"""




class SecondLargest:
    def __init__(self, input_list):
        self.input_list = input_list

    def second_largest(self):
        try:
            input_list = [int(item) for item in self.input_list.split(",")]

            # Ensure the list has at least two elements
            if len(input_list) < 2:
                print("List should have at least two elements.")
                return

            # Find the second largest element
            sorted_list = sorted(input_list)
            second_largest = sorted_list[-2]
            print("Orderd list:",sorted_list)
            print("Second largest element:", second_largest)

        except ValueError:
            print("Error: Enter valid integer values separated by commas.")

# Get user input for the items separated by commas
user_input = input("Enter the items separated by commas: ")

# Create an instance of SecondLargest
list_largest = SecondLargest(input_list=user_input)

list_largest.second_largest()

