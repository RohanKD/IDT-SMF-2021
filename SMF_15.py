"""
Rohan Dalal
25  February 2021
IDT
1st Period
SMF_14
"""
import random


def main():
    print('Would you like to play rock-paper-scissors')
    print('the rules are: you play until you lose, and you can choose wither rock, paper, or scissors')
    options = ['rock', 'paper', 'scissors']
    bot_life = 3
    lives = 3
    while ((lives > 0) and (bot_life > 0)):
        #both the coices are made
        choice = input('What do you choose').lower()
        x = random.randint(0, len(options) - 1)
        computer_choice = options[x]
        print("You chose: " + choice)
        #the choices are compared
        print("CPU chose: " + computer_choice)
        if (choice == 'rock'):
            if (computer_choice == choice):
                print('you tied')
            elif (computer_choice == 'paper'):
                print('You lose')
                lives = lives - 1
            elif (computer_choice == 'scissors'):
                print('You win')
                bot_life = bot_life - 1
        elif (choice == 'paper'):
            if (computer_choice == choice):
                print('you tied')
            elif (computer_choice == 'scissors'):
                print('You lose')
                lives = lives - 1
            elif (computer_choice == 'rock'):
                print('You win')
            bot_life = bot_life - 1
        elif (choice == 'scissors'):
            if (computer_choice == choice):
                print('you tied')
            elif (computer_choice == 'rock'):
                print('You lose')
                lives = lives - 1
            elif (computer_choice == 'paper'):
                print('You win')
                bot_life = bot_life - 1
        else:
            print("invalid option")
        #outcome is given
        ('Your lives are now:' + str(lives))
        ("CPU's lives are now:" + str(bot_life))
        #this has a ternary which chooses either life or lives depending on plurality
    if (bot_life == 0):
        print('GAME OVER, you win with ' + str(lives) + (" life" if lives == 1 else " lives") + ' left')
    else:
        print('GAME OVER!!, you lose and the bot still had ' + str(bot_life) + (" life" if bot_life == 1 else " lives") + ' left')


if (__name__ == '__main__'):
    main()
