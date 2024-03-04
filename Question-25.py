"""25.Quiz Game in Python"""


import time
import random

class QuizGame:
    def __init__(self, filename):
        # Initialize QuizGame object with the provided filename and an empty list for questions.
        self.filename = filename
        self.questions = []
        # Set the time limit for the quiz in seconds (15 minutes).
        self.quiz_time_limit = 900  

    def load_questions(self):
        try:
            # Try to open the file and read lines.
            with open(self.filename, 'r') as file:
                lines = file.readlines()

            # Process the lines to extract questions and answers.
            question_data = [line.strip() for line in lines if line.strip()]

            i = 0
            while i < len(question_data):
                try:
                    # Extract question text, options, and correct answer from the processed data.
                    question_text = question_data[i]
                    options = question_data[i + 1:i + 5]
                    correct_answer = question_data[i + 5]
                    question = {
                        'question_text': question_text,
                        'options': options,
                        'correct_answer': correct_answer
                    }
                    # Add the question to the list of questions.
                    self.questions.append(question)
                    i += 6
                except IndexError:
                    # Handle the case where there is not enough data for a complete question.
                    print(f"Error loading question at index {i}. Insufficient data for a complete question.")
                    break
        except FileNotFoundError:
            # Handle the case where the specified file is not found.
            print(f"File '{self.filename}' not found.")

    def run_quiz(self):
        if not self.questions:
            # Check if there are no questions loaded and exit the quiz if so.
            print("No questions loaded. Exiting.")
            return
        # Record the start time and calculate the end time based on the time limit.
        start_time = time.time()
        end_time = start_time + self.quiz_time_limit

        # Initialize variables to track the score, total questions, and question number.
        score = 0
        total_questions = len(self.questions)
        random.shuffle(self.questions)  # Shuffle questions 
        i = 0
        question_number = 1

        # Loop through the questions while there is time remaining.
        while i < len(self.questions) and time.time() < end_time:
            question = self.questions[i]
            # Display the current question number, text, and options.
            print(f"\nQuestion {question_number}/{total_questions}: {question['question_text']}")
            for option in question['options']:
                print(option)

            try:
                # Take user input for the answer and compare it with the correct answer.
                user_answer = input("Your answer: ")

                correct_answer = question['correct_answer'].split(":")[1].strip().lower()
                if user_answer == correct_answer:
                    # If the answer is correct, increment the score.
                    print("Correct!")
                    score += 1
                else:
                    # If the answer is wrong, provide the correct answer.
                    print(f"Wrong! The correct answer is {correct_answer}.")
            except KeyboardInterrupt:
                # Handle interruption (e.g., Ctrl+C) and exit the quiz.
                print("\nQuiz interrupted. Exiting.")
                break

            # Move to the next question.
            i += 1
            question_number += 1
        
        # Display quiz completion message, score, and pass/fail status.
        print(f"\nQuiz completed!\nYour score: {score}/{total_questions}")
        if time.time() >= end_time:
            # If time is up, print a message indicating the end of the quiz.
            print("\nTime's up! Quiz ended.")
        else:
            # If there is still time, evaluate pass/fail based on the score.
            if score >= 10:
                print("Congratulations! You passed the quiz!")
            else:
                print("Sorry, you didn't pass the quiz. Keep learning!")

try:
    # Attempt to run the quiz game.
    quiz_filename = "quiz_questions.txt"
    quiz_game = QuizGame(quiz_filename)
    print("Welcome to the Python Quiz!")
    print("Read each question carefully and choose the best answer to each one.")
    print("You have 15 minutes to answer the following questions.")
    quiz_game.load_questions()
    quiz_game.run_quiz()
except Exception as e:
    # Handle unexpected errors and print an error message.
    print(f"An unexpected error occurred: {e}")

