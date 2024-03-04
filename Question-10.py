"""Write a Python function that takes a list of numbers as input and returns 
the sum of all the numbers divisible by 3 or 5. """

class DivisibleBy:
    def __init__(self, list_input):
        self.list_input = list_input

    def sum_divisible_by_3_or_5(self):
        return sum(num for num in self.list_input if num % 3 == 0 or num % 5 == 0)

try:
    user_input = input("Enter a list of numbers separated by commas: ")
    input_numbers = [int(num) for num in user_input.split(",")]

    sum_calculator = DivisibleBy(list_input=input_numbers)

    # Calculate and print the result
    result = sum_calculator.sum_divisible_by_3_or_5()
    print(f"Input Numbers: {input_numbers}")
    print(f"Sum of Numbers Divisible by 3 or 5: {result}")

except ValueError:
    print("Error: Enter valid integers separated by commas.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
