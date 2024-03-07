# Rock,Paper,ScissorsGame
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

    def determine_winner(self, computer_choice, player1, player2=None, player3=None):
        # Determine the winner based on the game rules
        if player3 is not None:
            if player1 == player2 == player3:
                return "It's a tie!"

            elif (
                (player1 == "rock" and player2 == "scissors" and player3 == "scissors") or
                (player1 == "paper" and player2 == "rock" and player3 == "rock") or
                (player1 == "scissors" and player2 == "paper" and player3 == "paper")
            ):
                print("Player 1 wins!")
            elif (
                (player2 == "rock" and player1 == "scissors" and player3 == "scissors") or
                (player2 == "paper" and player1 == "rock" and player3 == "rock") or
                (player2 == "scissors" and player1 == "paper" and player3 == "paper")
            ):
                print("Player 2 wins!")
            elif (
                (player3 == "rock" and player1 == "scissors" and player2 == "scissors") or
                (player3 == "paper" and player1 == "rock" and player2 == "rock") or
                (player3 == "scissors" and player1 == "paper" and player2 == "paper")
            ):
                print("Player 3 wins!")
        elif player2 is not None:
            if player1 == player2:
                return "It's a tie!"
            elif (
                (player1 == "rock" and player2 == "scissors")
                or (player1 == "paper" and player2 == "rock")
                or (player1 == "scissors" and player2 == "paper")
            ):
                return "Player 1 wins!"
            else:
                return "Player 2 wins!"
        else:
            if player1 == computer_choice:
                return "It's a tie!"
            elif (
                (player1 == "rock" and computer_choice == "scissors")
                or (player1 == "paper" and computer_choice == "rock")
                or (player1 == "scissors" and computer_choice == "paper")
            ):
                return "Player 1 wins!"
            else:
                return "Computer wins!"

    def play_game(self, num_players):
        # Play a game with the specified number of players
        try:
            if num_players == 1:
                player1_choice = self.get_user_choice("Player 1")
                computer_choice = self.get_computer_choice()

                print(f"\nComputer's choice: {computer_choice}")

                result = self.determine_winner(computer_choice, player1_choice)
                print(result)

                if "Player 1" in result:
                    self.player1_score += 1
                elif "Computer" in result:
                    self.computer_score += 1

                print(f"Player 1 Score: {self.player1_score}")
                print(f"Computer Score: {self.computer_score}")
            elif num_players == 2:
                player1_choice = self.get_user_choice("Player 1")
                player2_choice = self.get_user_choice("Player 2")

                print(f"\nPlayer 1 choice: {player1_choice}")
                print(f"Player 2 choice: {player2_choice}")

                result = self.determine_winner(None, player1_choice, player2_choice)
                print(result)
                if "Player 1" in result:
                    self.player1_score += 1
                elif "Player 2" in result:
                    self.player2_score += 1

                print(f"Player 1 Score: {self.player1_score}")
                print(f"Player 2 Score: {self.player2_score}")
        

            elif num_players == 3:
                player1_choice = self.get_user_choice("Player 1")
                player2_choice = self.get_user_choice("Player 2")
                player3_choice = self.get_user_choice("Player 3")

                print(f"\nPlayer 1 choice: {player1_choice}")
                print(f"Player 2 choice: {player2_choice}")
                print(f"Player 3 choice: {player3_choice}")

                result = self.determine_winner(None, player1_choice, player2_choice, player3_choice)
                print(result)
                if "Player 1" in result:
                    self.player1_score += 1
                elif "Player 2" in result:
                    self.player2_score += 1
                elif "Player 3" in result:
                    self.player3_score += 1
                print(f"Player 1 Score: {self.player1_score}")
                print(f"Player 2 Score: {self.player2_score}")
                print(f"Player 3 Score: {self.player3_score}")
            # print(result)
            

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            
        

    def announce_winner(self):
        # Announce the overall winner based on the scores
        try:
           
            if hasattr(self, 'computer_score'):
                player_scores = [self.player1_score, self.player2_score, self.player3_score]
                max_score = max(player_scores + [self.computer_score])

                if max_score == self.computer_score:
                    print("Computer is the winner!")
                else:
                    winning_player = player_scores.index(max_score) + 1
                    print(f"Player {winning_player} is the winner!")

            else:
                max_score = max(self.player1_score, self.player2_score, self.player3_score)
                if max_score == self.player1_score:
                    print("Player 1 is the winner!")
                elif max_score == self.player2_score:
                    print("Player 2 is the winner!")
                else:
                    print("Player 3 is the winner!")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

print("Welcome to Rock, Paper, Scissors!")
print("\nChoose a game mode:")
print("1. 1 Player")
print("2. 2 Players")
print("3. 3 Players")

# while True:
try:
    choice = int(input("Enter your choice: "))
    if choice not in [1, 2, 3]:
        print("Invalid choice. Please enter 1, 2, or 3.")
        

    game = RockPaperScissorsGame()
    while True:
        if choice == 1:
            game.play_game(1)
        elif choice == 2:
            game.play_game(2)
        elif choice == 3:
            game.play_game(3)

        try:
            play_again = input("Do you want to continue playing? (yes/no): ").lower()
            if play_again not in ['yes', 'no']:
                raise ValueError("Invalid input. Please enter 'yes' or 'no'.")
        except ValueError as ve:
            print(f"Error: {ve}")

        if play_again != 'yes':
            game.announce_winner()
            print("Thanks for playing!")
            break

except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")