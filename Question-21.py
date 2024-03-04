"""21.Write a Python program that executes an operation on a list and handles an 
IndexError exception if the index is out of range."""



class ListOperator:
    def __init__(self, data):
        self.data = data

    def perform_operation(self):
      
        while True:
            try:
                # Get user input for index
                index_str = input("Enter an index (or 'q' to quit): ")

                # Check if user wants to quit
                if index_str.lower() == 'q':
                    print("Exiting...")
                    return

                # Convert input to integer
                index = int(index_str)

                # Check if index is within valid range
                if 0 <= index < len(self.data):
                    result = self.data[index]
                    print("The element at index", index, "is:", result)
                else:
                    print("IndexError: Index out of range. Please provide a valid index between 0 and", len(self.data) - 1)

            except ValueError:
                print("Invalid input. Please enter an integer or 'q' to quit.")

            # Ask the user if they want to continue
            user_choice = input("Do you want to continue? (yes/no): ").lower()
            if user_choice != 'yes':
                print("Exiting...")
                break

my_list = [10, 20, 30, 40, 50]
list_operator = ListOperator(my_list)
list_operator.perform_operation()


