"""17.Python program to delay printing of line from a file using sleep function"""


import time

class DelayedFile:
    def __init__(self):
        self.file_path = input("Enter the path to the file: ")
        self.delay_seconds = None

        try:
            self.delay_seconds = float(input("Enter the delay duration between lines (in seconds): "))
        except ValueError:
            print("Invalid input for delay duration. Please enter a valid number.")
            exit()

    def delayed_print(self):
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    print(line.strip())
                    time.sleep(self.delay_seconds)
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


try:
    delayed_printer = DelayedFile()
    delayed_printer.delayed_print()
except KeyboardInterrupt:
    print("\nOperation interrupted by the user.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

