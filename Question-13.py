"""13.Implement a program that simulates a basic calculator, allowing users to 
perform arithmetic operations (addition, subtraction, multiplication, 
division) on two numbers"""

class Calculator:
    def __init__(self, number1, number2, operator):
        self.number1 = number1
        self.number2 = number2
        self.operator = operator
        self.result = 0

    def calculate(self):
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
                return self.number1 ** self.number2
            else:
                return "Error: Enter a valid operation"
        except ZeroDivisionError as e:
            return str(e)
        except Exception as e:
            return f"An error occurred: {e}"
        
    def previous_calc(self, number3):
        try:
            self.result = self.result + number3
            print(f"Previous result + {number3} = {self.result}")
        except ValueError:
            print("Error: Enter a valid numeric input.")

while True:
    try:
        user_input1 = float(input("Enter the first number: "))
        user_input2 = float(input("Enter the second number: "))

        print("""Choose the operation to perform:
              1. Addition
              2. Subtraction
              3. Multiplication
              4. Division
              5. Floor division
              6. Modulus
              7. Exponentiation
              """)
        operation = int(input("Which operation do you need to perform (1/2/3/4/5/6/7): "))

        calc = Calculator(number1=user_input1, number2=user_input2, operator=operation)
        result = calc.calculate()

        print(f"{user_input1} {'+' if operation == 1 else '-' if operation == 2 else '*' if operation == 3 else '/' if operation == 4 else '//' if operation == 5 else '%' if operation == 6 else '**'} {user_input2} = {result}")

        # Ask the user if they want to continue
        user_choice = input("Do you want to continue with a new calculation or add to the previous result (new/add/exit)? ").lower()
        if user_choice == 'exit':
            print("Thank you for using. Exiting.")
            break
        elif user_choice == 'new':
             calc.calculate()
        elif user_choice == 'add':
             prev_number = int(input("Enter a number: "))
             calc.previous_calc(number3=prev_number)

    except ValueError:
        print("Error: Enter valid numeric input.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


