import random
import keyboard

input("""
WELCOME TO CRAPS!

The rules of the game:

The player should roll two dice. If the sum of both of them is
7 or 11 the player wins. If the sum is 2, 3 or 12 (craps) the 
casino wins. If during the first roll the sum is 4, 5, 6, 8,
9 or 10, that number becomes the “goal” number. To win, the player
should roll the dice till they roll the goal number again. If the 
player rolls a 7 before rolling the goal number, they lose.

Press Enter to start the game.
""")

game = True
while game:
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    sum = dice_1 + dice_2
    input('Press Enter to roll the dice. ')
    print(f'{dice_1} + {dice_2} = {sum}')

    if sum in [7, 11]:
        print('You win!')
    elif sum in [2, 3, 12]:
        print('Craps. You lost!')

    print("""If you want to play again press 'Enter', 
If not, press 'Esc' to exit the game.""")

    while True:
        key = keyboard.read_key()
        if key == 'enter':
            game = True
            break
        elif key == 'esc':
            print('Thanks for playing.')
            game = False
            break
