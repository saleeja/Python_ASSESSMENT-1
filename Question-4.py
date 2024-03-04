"""4. Merge Multiple Text Files into One"""

def merge_text_files():
    try:
        # Get the number of files to merge
        num_files = int(input("Enter the number of files to merge: "))

        # Create a list to store input file paths
        input_files = []

        # Loop to get input file paths
        for i in range(num_files):
            file_name = input(f"Enter the path of file {i + 1}: ")
            input_files.append(file_name)

        # Ask the user if they want to merge into an existing file
        merge_option = input("Do you want to merge into an existing file? (yes/no): ").lower()

        # Get the name of the output file
        output_file = input("Enter the name of the output file: ")

        # Open the output file in 'a' (append) or 'w' (write) mode based on user choice
        with open(output_file, 'a' if merge_option == 'yes' else 'w') as output:
            # Loop through each input file and append its content to the output file
            for input_file in input_files:
                with open(input_file, 'r') as file:
                    output.write(file.read() + '\n')

        print(f"Files merged successfully. Output saved to {output_file}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except FileNotFoundError:
        print("One or more input files not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
merge_text_files()


