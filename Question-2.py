"""2. Count the Number of Lines, Words, and Characters in a Text File"""

class CountTextFile:
    def __init__(self, file_name):
        # Initialize the CountTextFile object with the provided file name.
        self.file_name = file_name

    def count_file(self):
        try:
            # Try to open and read the contents of the file.
            with open(self.file_name, "r") as file:
                contents = file.read()

                # Count lines
                lines = contents.split('\n')
                num_lines = len(lines)

                # Count words
                words = contents.split()
                num_words = len(words)

                # Count characters
                num_characters = len(contents)

                # Print the counts
                print(f"Number of lines: {num_lines}")
                print(f"Number of words: {num_words}")
                print(f"Number of characters: {num_characters}")

        except FileNotFoundError:
            # Handle the case where the specified file is not found.
            print(f"The file '{self.file_name}' does not exist.")
        except Exception as e:
            # Handle other unexpected errors and print an error message.
            print(f"An error occurred while analyzing the file: {e}")

# Get user input for the file name.
file_path = input("Enter the file name to count:")
# Create a CountTextFile object with the provided file name.
file_manager = CountTextFile(file_name=file_path)
# Count and display the lines, words, and characters in the file.
file_manager.count_file()

