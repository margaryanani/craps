import random

input("""
WELCOME TO CRAPS!

The rules of the game:

The player should roll two dice. If the sum of both of them is
7 or 11 the player wins. If the sum is 2, 3 or 12 (craps) the 
casino wins. If during the first roll the sum is 4, 5, 6, 8,
9 or 10, that number becomes the “goal” number. To win, the player
should roll the dice till they roll the goal number again. If the 
player rolls a 7 before rolling the goal number, they lose.

Your balance will be 100$. Before rolling the dice you'll make a bet.

Press Enter to start the game.
""")

balance = 100

game = True
while game:
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    sum_1 = dice_1 + dice_2
    bet = int(input("How much would you like to bet? "))
    while bet > balance:
        bet = int(input(f"Your balance is {balance}$. You can bet {balance}$ or less. Try again.  "))
        if bet <= balance:
            input('Press Enter to roll the dice. ')
            input(f'{dice_1} + {dice_2} = {sum_1}')
            if sum_1 in [7, 11]:
                print('You win!')
                balance = balance + bet
                print(f'Your balance is {balance}$')
            elif sum_1 in [2, 3, 12]:
                print('Craps. You lost!')
                balance = balance - bet
                print(f'Your balance is {balance}$')
            elif sum_1 in [4, 5, 6, 8, 9, 10]:
                print("Goal!")
                dice_1 = random.randint(1, 6)
                dice_2 = random.randint(1, 6)
                sum_2 = dice_1 + dice_2
                print(f'{dice_1} + {dice_2} = {sum_2}')
                while sum_2 != 7:
                    dice_1 = random.randint(1, 6)
                    dice_2 = random.randint(1, 6)
                    sum_2 = dice_1 + dice_2
                    input(f'{dice_1} + {dice_2} = {sum_2}')
                    if sum_2 == 7:
                        print('You lose!')
                        balance = balance - bet
                        print(f'Your balance is {balance}$')
                        break
                    elif sum_2 == sum_1:
                        print('You win!')
                        balance = balance + bet
                        print(f'Your balance is {balance}$')
                        break
            if balance <= 0:
                print("You don't have any money to continue.")
                game = False
            elif balance > 0:
                print('do you want to play again?')
                answer = input("If you want to continue Enter 'yes', if not, enter 'no'> ")
                if answer == 'yes':
                    game = True
                elif answer == 'no':
                    print('Thank you for playing!')
                    print(f'Your total balance is {balance}$')
                    game = False
                elif balance <= 0:
                    print("You don't have any money to continue.")
                    game = False
