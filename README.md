# Craps
## Introduction
A classic game of craps with a betting system.

## How to download files

- ### Downloading Individual Files
  - Click on the file that you want to download.
  - Click the download icon, which lets you download the raw file or right-click the "Raw" button and select "Save link as..." to download the file.
- ### Cloning the Repository
  If you want to work with the entire repository and want to make changes, cloning is the best option.
  
  - Make sure that you have Git installed on your computer.
  - Open a terminal.
  - Navigate to the directory where you want to clone the repository.
  - Run this command. `git clone https://github.com/margaryanani/craps.git`
 
## Usage

For this project you need 'craps_class.py' and 'craps.py' to run the game. The 'craps_class.py' contains a class with its functions and 'craps.py' is used to execute the game. After downloading both files, run the 'craps.py' file and the game will start.

## Code Structure
### 'craps_class.py'

In this file we have a class called 'Craps' that contains everything for the game to work.

- `__init__(self)` method contains `self.balance` which is set to 100$, `self.game_over = False` is used for tracking whether or not the game has ended and `self.goal = None` is used for tracking if the user rolled a goal number or not.
- The `dice_roll(self)` function rolls the 2 dice and returns their sum.
- The `place_bet(self)`  function lets the user to make a bet and tracks whether or not the user entered the right input (The wrong inputs would be: betting more than their balance, entering a negetive number, entering anything besides an integer).
- The `game(self)` function is for rolling the dice and determining the outcome of the first roll to see if the user won, lost or rolled a goal number. If the user won, their balance is incremented by the bet they initially put at the start of the game, if they lost, the bet is subtracted from the balance. On the both cases that round of the game ends. If the user rolled a 'goal' number `self.goal` is set to `roll`. So the user has to roll the dice till the goal number or 7.
- The `roll_till_goal_or_seven(self, bet)` function is for the case when the user rolls a goal number in the first roll. The function keeps asking the user to roll a dice till the goal number or 7. If the user rolls the goal number they win and their balance is incremented by the bet, if they lose, the bet is subtracted and the round ends.
- The `play(self)` functions starts the game with an introduction, checks the balance and prints the balance after a round. Asks the user if they want to continue playing, that also tracks for the right input. If the user wants to continue the function starts another round, if the user doesn't want to continue, the game ends. If user's balance is 0 or less the game ends.

