"""13.Implement a program that simulates a basic calculator, allowing users to 
perform arithmetic operations (addition, subtraction, multiplication, 
division) on two numbers"""


class Calculator:
    def __init__(self, number1, number2):
        # Initialize the Calculator with two numbers, an operator, and a result
        self.number1 = number1
        self.number2 = number2
        self.operator = None
        self.result = 0

    def calculate(self):
        # Perform the calculation based on the selected operator
        try:
            if self.operator == 1:
                return self.number1 + self.number2
            elif self.operator == 2:
                return self.number1 - self.number2
            elif self.operator == 3:
                return self.number1 * self.number2
            elif self.operator == 4:
                if self.number2 != 0:
                    return self.number1 / self.number2
                else:
                    raise ZeroDivisionError("Error: Division by zero")
            elif self.operator == 5:
                return self.number1 // self.number2
            elif self.operator == 6:
                return self.number1 % self.number2
            elif self.operator == 7:
                return self.number1**self.number2
            else:
                raise ValueError("Error: Enter a valid operation")
        except ZeroDivisionError as e:
            return str(e)
        except Exception as e:
            return f"An error occurred: {e}"

    def previous_calc(self, number3):
        # Perform a calculation using the previous result and a new number
        try:
            if self.operator == 1:
                self.result += number3
                print(f"Previous result + {number3} = {self.result}")
            elif self.operator == 2:
                self.result -= number3
                print(f"Previous result - {number3} = {self.result}")
            elif self.operator == 3:
                self.result *= number3
                print(f"Previous result * {number3} = {self.result}")
            elif self.operator == 4:
                if number3 != 0:
                    self.result /= number3
                    print(f"Previous result / {number3} = {self.result}")
                else:
                    raise ZeroDivisionError("Error: Division by zero")
            elif self.operator == 5:
                self.result //= number3
                print(f"Previous result // {number3} = {self.result}")
            elif self.operator == 6:
                self.result %= number3
                print(f"Previous result % {number3} = {self.result}")
            elif self.operator == 7:
                self.result **= number3
                print(f"Previous result ** {number3} = {self.result}")
            else:
                raise ValueError("Error: Enter a valid operation")
        except ValueError:
            print("Error: Enter a valid numeric input.")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def operations(self):
        # Display a menu of operations and prompt the user to select one
        print(
            """Choose the operation to perform:
              1. Addition
              2. Subtraction
              3. Multiplication
              4. Division
              5. Floor division
              6. Modulus
              7. Exponentiation
              """
        )
        self.operator = int(
            input("Which operation do you need to perform (1/2/3/4/5/6/7): ")
        )


# Main loop for user interaction
while True:
    try:
        # Get user input for two numbers
        user_input1 = float(input("Enter the first number: "))
        user_input2 = float(input("Enter the second number: "))

        # Create a Calculator instance with the provided numbers
        calc = Calculator(number1=user_input1, number2=user_input2)

        # Prompt the user to select an operation
        calc.operations()

        # Perform the calculation and display the result
        result = calc.calculate()
        print(
            f"{user_input1} {'+' if calc.operator == 1 else '-' if calc.operator == 2 else '*' if calc.operator == 3 else '/' if calc.operator == 4 else '//' if calc.operator == 5 else '%' if calc.operator == 6 else '**'} {user_input2} = {result}"
        )

        # Allow the user to continue with a new calculation or add to the previous result
        while True:
            user_choice = input(
                "Do you want to continue with a new calculation or add to the previous result (new/add/exit)? "
            ).lower()
            if user_choice == "exit":
                break
            elif user_choice == "new":
                break
            elif user_choice == "add":
                # Prompt the user for a new number and perform a calculation using the previous result
                calc.operations()
                new_number = float(input("Enter a number: "))
                calc.previous_calc(number3=new_number)

        # Check if the user chose to exit
        if user_choice == "exit":
            print("Thank you for using. Exiting.")
            break

    except ValueError:
        print("Error: Enter valid numeric input.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
