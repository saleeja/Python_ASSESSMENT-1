"""1.Read and Print the Contents of a Text File"""


class TextFileContent:
    def __init__(self, file_name):
        # Initialize the TextFileContent object with the provided file name.
        self.file_name = file_name

    def read_file(self):
        try:
            # Try to open and read the contents of the file.
            with open(self.file_name, "r") as file:
                contents = file.read()
                # Print the content of the file.
                print("The file content is:")
                print(contents)
        except FileNotFoundError:
            # Handle the case where the specified file is not found.
            print(f"File not found: {self.file_name}")
        except Exception as e:
            # Handle other unexpected errors and print an error message.
            print(f"An error occurred: {e}")

# Get user input for the file name.
file_input = input("Enter the file to read:")
# Create a TextFileContent object with the provided file name.
file_manager = TextFileContent(file_name=file_input)
# Read and display the content of the file.
file_manager.read_file()
