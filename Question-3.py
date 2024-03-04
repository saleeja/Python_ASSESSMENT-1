"""3.Search for a String in a Text File"""

class SearchFile:
    def __init__(self, file_name):
        # Initialize the SearchFile object with the provided file name.
        self.file_name = file_name

    def search_string(self, target_string, count_occurrences=False, display_line_numbers=False, print_matching_lines=False):
        try:
            # Try to open and read the contents of the file.
            with open(self.file_name, "r") as file:
                contents = file.read()
                lower_target = target_string.lower()
                lower_contents = contents.lower()

                # Search for the target string
                if lower_target in lower_contents:
                    print(f"Found '{target_string}' in the file.")

                    # Count occurrences
                    if count_occurrences:
                        occurrences = lower_contents.count(lower_target)
                        print(f"Number of occurrences: {occurrences}")

                    # Display line numbers
                    if display_line_numbers:
                        lines = contents.split('\n')
                        matching_line_numbers = [i + 1 for i, line in enumerate(lines) if lower_target in line.lower()]
                        print(f"Matching line numbers: {matching_line_numbers}")

                else:
                    print(f"'{target_string}' not found in the file.")

        except FileNotFoundError:
            # Handle the case where the specified file is not found.
            print(f"The file '{self.file_name}' does not exist.")
        except Exception as e:
            # Handle other unexpected errors and print an error message.
            print(f"An error occurred while searching the file: {e}")

# Get user input for the file name and the target string to search.
file_path = input("Enter the file name to search:")
search_string = input("Enter the string to search for:")
# Create a SearchFile object with the provided file name.
file_searcher = SearchFile(file_name=file_path)
# Search for the target string and display results based on user preferences.
file_searcher.search_string(target_string=search_string, count_occurrences=True, display_line_numbers=True, print_matching_lines=True)
