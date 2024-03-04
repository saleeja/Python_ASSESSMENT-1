"""8.Write a Python program that takes a list of integers as input and returns a 
new list with only the numbers that are prime."""




class PrimeNumber:
    def __init__(self, list_input):
        self.list_input = list_input

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def filter_primes(self):
        return [num for num in self.list_input if self.is_prime(num)]

try:
    # Get user input for the list of integers separated by commas
    user_input = input("Enter the list of integers separated by commas: ")

    # Convert input to a list of integers
    input_list = [int(item) for item in user_input.split(",")]

    # Create an instance of the PrimeNumber class
    prime_obj = PrimeNumber(list_input=input_list)

    # Apply the filter_primes method to get the prime numbers
    prime_numbers = prime_obj.filter_primes()

    # Display the result
    print("Original list:", input_list)
    if prime_numbers:
        print("Prime numbers:", prime_numbers)
    else:
        print("No prime numbers in the list")

except ValueError:
    print("Error: Enter valid integers separated by commas.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")





