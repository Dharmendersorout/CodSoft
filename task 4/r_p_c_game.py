import numpy as np

class RPCgame:
      def __init__(self):
            print(""" 
            Welcome to the Rock, Paper, Scissors Game!
            Rock beats Scissors, Scissors beat Paper, and Paper beats Rock.
            Let's see if you can beat the computer!
            """)
            
            self.user_score = 0
            self.computer_score = 0
            self.play_game()

      def __decor(func):
            def wrapper(*args, **kwargs):
                  print("-------------------------------------------------------")
                  result = func(*args, **kwargs)  # Ensure the decorated function executes correctly
                  print("-------------------------------------------------------")
                  return result
            return wrapper

      @__decor
      def __userinp(self):
            user = input(""" 
            What is your choice?
            1. Rock
            2. Paper
            3. Scissors
                              
            Input: """).strip().lower()

            if user in ['1', 'rock']:
                  return 'rock'
            elif user in ['2', 'paper']:
                  return 'paper'
            elif user in ['3', 'scissors']:
                  return 'scissors'
            else:
                  print("Invalid input. Please try again.")
                  return self.__userinp()

      def __compinp(self):
            return np.random.choice(['rock', 'paper', 'scissors'])

      def __check(self):
            user = self.__userinp()
            comp = self.__compinp()
            print(f"You picked: {user}")
            print(f"Computer picked: {comp}")

            if user == comp:
                  print("It's a tie!")
                  return "tie"
            elif (user == 'rock' and comp == 'scissors') or \
                  (user == 'paper' and comp == 'rock') or \
                  (user == 'scissors' and comp == 'paper'):
                  print("You Win this round!")
                  return "user"
            else:
                  print("Computer Wins this round!")
                  return "computer"

      def play_game(self):
            while True:
                  result = self.__check()  # Call check directly
                  if result == "user":
                        self.user_score += 1
                  elif result == "computer":
                        self.computer_score += 1

                  print("-------------------------------------------------------")
                  print(f"Score: You - {self.user_score}, Computer - {self.computer_score}")
                  print("-------------------------------------------------------")
                  
                  play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
                  if play_again not in ['yes', 'y']:
                        print("-------------------------------------------------------")
                        print("\nFinal Scores:")
                        print(f"You: {self.user_score}")
                        print(f"Computer: {self.computer_score}")
                        print("-------------------------------------------------------")
                        if self.user_score > self.computer_score:
                              print("Congratulations! You won the game!")
                        elif self.user_score < self.computer_score:
                              print("Better luck next time! Computer wins the game.")
                        else:
                              print("It's a tie overall!")
                        print("Thanks for playing! Goodbye!")
                        print("-------------------------------------------------------")
                        break

obj = RPCgame()
