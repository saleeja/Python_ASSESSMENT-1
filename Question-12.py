"""12.Write a function that takes a sentence as input and returns a new sentence 
with the words reversed, while keeping the order of the words in the 
sentence."""


class ReverseWord:
    def __init__(self, user_string):
        """
        Initialize the ReverseWord class.

        Parameters:
        - user_string (str): The input sentence provided by the user.
        """
        self.user_string = user_string

    def reversed_word(self):
        """
        Reverse each word in the sentence and join them to form a reversed sentence.

        Returns:
        - str: The reversed sentence.
        """
        try:
            reversed_sentence = ' '.join(word[::-1] for word in self.user_string.split(" "))
            return reversed_sentence
        except Exception as e:
            return f"An error occurred: {e}"

try:
    user_input = input("Enter a sentence: ")
    reverse_obj = ReverseWord(user_string=user_input)
    result = reverse_obj.reversed_word()
    print(result)
except KeyboardInterrupt:
    print("\nOperation interrupted by the user.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


