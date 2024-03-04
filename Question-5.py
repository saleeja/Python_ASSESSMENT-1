"""Implement a program that reads a text file and counts the occurrences of 
each word, ignoring case sensitivity"""


from collections import Counter

class WordCounter:
    def __init__(self, file_name):
        self.file_name = file_name

    def count_words(self):
        try:
            with open(self.file_name, "r") as file:
                contents = file.read()
                lower_contents = contents.lower()
                

                words = lower_contents.split()
                num_words = len(words)
                print(f"Number of words: {num_words}")

                lines = contents.split('\n')
                num_lines = len(lines)
                print(f"Number of lines: {num_lines}")

                
                # Count occurrences of each unique word
                word_counts = Counter(words)
                print("Word occurrences:")
                for word, count in word_counts.items():
                    print(f"{word}: {count}")

                # Count occurrences of each unique word
                word_counts = Counter(words)
                print("Word occurrences:")
                for word, count in word_counts.items():
                    print(f"{word}: {count}")

                # Find the most common word(s)
                most_common_words = word_counts.most_common()
                max_count = most_common_words[0][1]
                common_words = [word for word, count in most_common_words if count == max_count]

                print(f"\nMost common word(s): {', '.join(common_words)} (occurs {max_count} times)")

                

        except FileNotFoundError:
            print(f"The file '{self.file_name}' does not exist.")
        except Exception as e:
            print(f"An error occurred while analyzing the file: {e}")

# Get user input for the file name
user_file_input = input("Enter file name: ")

# Create an instance of WordCounter
word_counter = WordCounter(file_name=user_file_input)

# Call the count_words method
word_counter.count_words()


