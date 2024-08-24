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
        print(f"{roll} = {dice_1} + {dice_2}")
        return roll

    def place_bet(self):
        while True:
            try:
                bet = int(input("Place your bet: "))
                if bet > self.balance:
                    print("You don't have enough money.")
                elif bet <= 0:
                    print("You must place a positive bet.")
                else:
                    return bet
            except ValueError:
                print("Invalid input. Enter a valid number.")

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
                print(f"Your goal is now {self.goal}.")
                self.roll_till_goal_or_seven(bet)

    def roll_till_goal_or_seven(self, bet):
        while not self.game_over:
            input('Press enter to roll again. ')
            roll = self.dice_roll()
            if roll == self.goal:
                self.balance += bet
                print(f"You rolled your goal number {self.goal} and win!")
                self.game_over = True
            elif roll == 7:
                self.balance -= bet
                print("You rolled a 7 and lose!")
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
            self.game_over = False
            self.game()
            if self.balance > 0:
                print(f"Your current balance is ${self.balance}.")
                if input("Would you like to play again? (y/n): ").lower() != 'y':
                    break
            else:
                print("You don't have enough money.")


if __name__ == "__main__":
    game = Craps()
    game.play()

