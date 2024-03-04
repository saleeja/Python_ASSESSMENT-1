
import random

def generate_unique_id(user_initials):
    random_number = random.randint(1000, 9999)  # Generate a random 4-digit number
    unique_id = f"{user_initials.upper()}{random_number}"
    return unique_id

def input_with_expectation(prompt, expected_type, error_message="Invalid input. Please try again."):
    while True:
        try:
            user_input = expected_type(input(prompt))
            return user_input
        except ValueError:
            print(error_message)






