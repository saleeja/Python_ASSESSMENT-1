"""Write a Python function that takes a list of integers as input and returns a 
new list with only the numbers that are perfect squares.""" 

class PerfectSquares:
  """
  This class finds perfect squares in a list of integers.
  """
  def __init__(self):
    self.num_list = []

  def get_list_input(self):
    """
    Gets a list of integers from user input.
    """
    while True:
      try:
        # Get comma-separated integer input
        user_input = input("Enter a list of integers separated by commas: ")
        # Split the input string into a list of integers
        self.num_list = [int(num) for num in user_input.split(",")]
        break
      except ValueError:
        print("Invalid input. Please enter comma-separated integers.")

  def find_perfect_squares(self):
    """
    This method finds perfect squares in the list and stores them in a new list.
    """
    perfect_squares = []
    for num in self.num_list:
      # Check if the square root is an integer
      if int(num**0.5) ** 2 == num:
        perfect_squares.append(num)
    return perfect_squares

  def print_results(self):
    """
    Prints the original list and the list of perfect squares.
    """
    print("Original list:", self.num_list)
    print("Perfect squares:", self.find_perfect_squares())

try:
    # Create an instance of PerfectSquares
    perfect_squares = PerfectSquares()

    # Get user input for the list
    perfect_squares.get_list_input()

    # Print the results
    perfect_squares.print_results()

except Exception as e:
    print(f"An unexpected error occurred: {e}")



