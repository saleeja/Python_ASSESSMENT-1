"""2.Write a Python program input and add two integers only and handle the 
exceptions.
RUN 1:
Enter First Value: 10
Enter Second Value: 20
0.5
RUN 2:
Enter First Value: 10
Enter Second Value: Hello
Pls Input Integer Only invalid literal for int() with base 10: 'Hello'
RUN 3:
Enter First Value: 10
Enter Second Value: 0
Second Number Should Not Be Zero division by zero"""

def add_two_integers():
    while True:
        try:
            # Get user input for the first value
            first_value = int(input("Enter First Value: "))

            # Get user input for the second value
            second_value = int(input("Enter Second Value: "))

            # Check if the second value is zero
            if second_value == 0:
                raise ValueError("Second Number Should Not Be Zero")

            # Perform the addition
            result = first_value / second_value

            # Print the result
            print(result)
            break  # Exit the loop after successful execution

        except ValueError as ve:
            print(f"Pls Input Integer Only {ve}")
        except ZeroDivisionError as zde:
            print(f"Second Number Should Not Be Zero {zde}")


add_two_integers()
