import random

class RockPaperScissorsGame:
    def __init__(self):
        # Initialize the game with choices and scores for each player
        self.choices = ["rock", "paper", "scissors"]
        self.player1_score = 0
        self.player2_score = 0
        self.player3_score = 0
        self.computer_score = 0

    def get_user_choice(self, player_name):
        # Get and validate user input for the player's choice
        while True:
            try:
                print(f"{player_name}, enter your move (rock, paper, or scissors): ")
                user_choice = input().lower()

                if user_choice not in self.choices:
                    raise ValueError("Invalid choice. Please enter rock, paper, or scissors.")

                return user_choice
            except ValueError as e:
                print(f"Error: {e}")

    def get_computer_choice(self):
        # Generate a random choice for the computer player
        return random.choice(self.choices)

    def determine_winner(self, player_choice, opponent_choice):
        # Determine the winner based on the game rules
        if player_choice == opponent_choice:
            return "It's a tie!"
        elif (
            (player_choice == "rock" and opponent_choice == "scissors")
            or (player_choice == "paper" and opponent_choice == "rock")
            or (player_choice == "scissors" and opponent_choice == "paper")
        ):
            return f"{player_choice.capitalize()} wins!"
        else:
            return f"{opponent_choice.capitalize()} wins!"

    def play_1_player_game(self):
        # Play a game with one player against the computer
        try:
            player1_choice = self.get_user_choice("Player 1")
            computer_choice = self.get_computer_choice()

            print(f"\nComputer's choice: {computer_choice}")

            result = self.determine_winner(player1_choice, computer_choice)
            print(result)

            if "wins" in result:
                self.player1_score += 1
            elif "Computer" in result:
                self.computer_score += 1

            print(f"Player 1 Score: {self.player1_score}")
            print(f"Computer Score: {self.computer_score}")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

   

    def announce_winner(self):
        # Announce the overall winner based on the scores
        try:
            player_scores = [self.player1_score, self.player2_score, self.player3_score]
            max_score = max(player_scores + [self.computer_score])

            if max_score == self.computer_score:
                print("Computer is the winner!")
            else:
                winning_player = player_scores.index(max_score) + 1
                print(f"Player {winning_player} is the winner!")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

print("Welcome to Rock, Paper, Scissors!")
print("\nChoose a game mode:")
print("1. 1 Player")
print("2. 2 Players")
print("3. 3 Players")

while True:
    game = RockPaperScissorsGame()

    try:
        choice = input("Enter your choice: ")
        while True:
            if choice == "1":
                game.play_1_player_game()
            elif choice == "2":
                game.play_2_player_game()
            elif choice == "3":
                game.play_3_player_game()
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

            play_again = input("Do you want to continue playing? (yes/no): ").lower()

            if play_again != 'yes':
                game.announce_winner()
                print("Thanks for playing!.")
                break

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


