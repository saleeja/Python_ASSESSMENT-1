"""23.The program takes input from the user and checks if whether the input 
value is an integer or not, if the input value is not an integer then the 
program will through a Type exception.
Run 1: 
Enter First Number: 43
43
Run 2:
Enter First Number: 123.1
Invalid Input..Please Input Integer Only..
Enter First Number: 43
43
"""

def get_integer_input():
    while True:
        try:
            # Get user input for the first number
            user_input = input("Enter First Number: ")

            # Try converting the input to an integer
            integer_value = int(user_input)

            # If successful, print the integer value and exit the loop
            print(integer_value)
            break

        except ValueError:
            print("Invalid Input. Please Input Integer Only.")

get_integer_input()
