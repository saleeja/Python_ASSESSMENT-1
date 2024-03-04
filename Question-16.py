"""16.Count the total number of uppercase characters in a file in Python"""

def count_uppercase_characters(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            uppercase_count = sum(1 for char in content if char.isupper())
            return uppercase_count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return 0

file_path = "Bio.txt"  
uppercase_count = count_uppercase_characters(file_path)
print(f"Total number of uppercase characters in the file: {uppercase_count}")
