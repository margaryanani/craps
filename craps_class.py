import random


class Craps:
    def __init__(self):
        self.balance = 100
        self.game_over = False
        self.goal = None

    def dice_roll(self):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        roll = dice_1 + dice_2
        print(f"{dice_1} + {dice_2} = {roll}")
        return roll

    def place_bet(self):
        while True:
            try:
                bet = int(input("Place your bet: "))
                if bet > self.balance:
                    print(f"""
You don't have enough money.
Your balance is ${self.balance}""")
                elif bet <= 0:
                    print("You must enter a positive number.")
                else:
                    return bet
            except ValueError:
                print("Invalid input. Enter a valid number(int).")

    def game(self):
        while not self.game_over:
            bet = self.place_bet()
            roll = self.dice_roll()

            if roll in [7, 11]:
                self.balance += bet
                print("You win!")
                self.game_over = True
            elif roll in [2, 3, 12]:
                self.balance -= bet
                print("You lose!")
                self.game_over = True
            elif roll in [4, 5, 6, 8, 9, 10]:
                self.goal = roll
                print(f"Your goal is set to {self.goal}.")
                self.roll_till_goal_or_seven(bet)

    def roll_till_goal_or_seven(self, bet):
        while not self.game_over:
            input('Press enter to roll again. ')
            roll = self.dice_roll()
            if roll == self.goal:
                self.balance += bet
                print(f"Goal! You win!")
                self.game_over = True
            elif roll == 7:
                self.balance -= bet
                print("7! You lose!")
                self.game_over = True

    def play(self):
        input("""
WELCOME TO CRAPS!

The rules of the game:

The player should roll two dice. If the sum of both of them is
7 or 11 the player wins. If the sum is 2, 3 or 12 (craps) the 
casino wins. If during the first roll the sum is 4, 5, 6, 8,
9 or 10, that number becomes the “goal” number. To win, the player
should roll the dice till they roll the goal number again. If the 
player rolls a 7 before rolling the goal number, they lose.

Your balance will be $100. Before rolling the dice you'll make a bet.

Press Enter to start the game.
""")

        while self.balance > 0:
            self.game()
            if self.balance > 0:
                print(f"Your current balance is ${self.balance}.")
                while True:
                    answer = input("Do you want to play again? (yes/no) ")
                    if answer == "yes":
                        self.game_over = False
                        break
                    elif answer == "no":
                        self.game_over = True
                        break
                    else:
                        print("Invalid input. Enter yes or no.")
            else:
                print("You don't have enough money.")


if __name__ == "__main__":
    game = Craps()
    game.play()
