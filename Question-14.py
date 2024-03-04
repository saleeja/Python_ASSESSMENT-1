"""14.Create a class named Notes for handling text-based file operations. Class 
should contain methods "write", "read" and then "append" as instance 
methods or class methods. (Can contain any other methods if you wish) 
Use a single file for saving the notes. You can set the file name as a constant 
somewhere in the program (Or as a class variable). write method should 
create the if it doesn't exist, Then it should overwrite the older contents 
with the user input if the user plans to overwrite the file. read method 
should read the whole file contents and return it. If the file doesn't exist, 
then it should return "No notes found" append method should take the 
user input value and it must add the value to the end of the file. It must not 
overwrite the file. Now create a program to utilize this class. 
The program should repeatedly ask the user for these 4 choices : 
1 - Write Note (Overwrite existing). 
2 - Add more Notes (Append). 
3 - Read Notes. 
4 – Exit"""


class Notes:
    FILE_NAME = "notes.txt"  # Constant file name

    @classmethod
    def write(cls, content):
        """
        Write content to the file, overwriting existing content.

        Parameters:
        - content (str): The content to be written to the file.
        """
        try:
            with open(cls.FILE_NAME, "w") as file:
                file.write(content)
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")

    @classmethod
    def read(cls):
        """
        Read the entire content from the file.

        Returns:
        - str: The content of the file, or "No notes found" if the file doesn't exist.
        """
        try:
            with open(cls.FILE_NAME, "r") as file:
                return file.read()
        except FileNotFoundError:
            return "No notes found"
        except Exception as e:
            return f"An error occurred while reading from the file: {e}"

    @classmethod
    def append(cls, content):
        """
        Append content to the end of the file.

        Parameters:
        - content (str): The content to be appended to the file.
        """
        try:
            with open(cls.FILE_NAME, "a") as file:
                file.write(content + "\n")
        except Exception as e:
            print(f"An error occurred while appending to the file: {e}")


def main():
    while True:
        print("\nChoose an option:")
        print("1. Write Note (Overwrite existing)")
        print("2. Add more Notes (Append)")
        print("3. Read Notes")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            content = input("Enter the note to overwrite existing content: ")
            Notes.write(content)
        elif choice == "2":
            content = input("Enter the note to append: ")
            Notes.append(content)
        elif choice == "3":
            content = Notes.read()
            print(content)
        elif choice == "4":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


main()



