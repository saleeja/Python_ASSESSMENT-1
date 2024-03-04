"""15.Copy odd lines of one file to another file in Python"""


def copy_odd_lines(input_file, output_file):
    try:
        with open(input_file, 'r') as file_in, open(output_file, 'w') as file_out:
            lines = file_in.readlines()
            odd_lines = [line for i, line in enumerate(lines, start=1) if i % 2 != 0]
            file_out.writelines(odd_lines)
        print(f"Odd lines copied from '{input_file}' to '{output_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")

# Get user input for file paths
input_file_path = input("Enter the path of the input file: ")
output_file_path = input("Enter the path of the output file: ")

copy_odd_lines(input_file_path, output_file_path)
