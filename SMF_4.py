"""
Rohan Dalal
20 January 2021
IDT
1st Period
SMF_3
"""
"""This is where I imported the libraries, the on i used was the random library
which i used for generating random numbers for my dice rolls"""
import os, sys
import cs50
import random

def main():
    # here i asked if they wanted to play the game or not
    x = input('Would you like to play a game of chance')
    # if they said yes i executed the following code, which tells them the rules and how the game works
    if(x==' yes'):
        print('Ok here are the rules, you start out with 18 dollars, each dice roll cost 6 dollars to play. You then roll 3 dice at once which costs 18 dollars.')
        print('The number on each dice roll is squared, and if it is less than 10 you lose that amount ')
        # if the user did not say yes the following code will be executed
    else:
        print('Ok you win nothing')
         # this asks the user if they want to roll the dice
    y = input('Do you want to roll the dice')
    # if they wanted to roll the dice, the dice would be rolled using a pseudo rnadom number generator
    if(y==' yes'):
    # dice one is rolled
        diceOne= (random.randint(1,6))
    # dice two is rolled
        diceTwo= (random.randint(1,6))
    # dice three is rolled
        diceThree= (random.randint(1,6))



        # this tell them what dice numbers were rolled
    print('You rolled a '+ str(diceOne) +', '+ str(diceTwo) +',and a '+str(diceThree))
        #here the score for the first die is added to the score
    if (diceOne >= 4):
    # if the dice roll is higher than 3 its square gets added to the score
        score= diceOne**2
        # Otherwise it gets subtracted from the score
    else:
        score= (diceOne**2)*-1
         #here the score for the second die is added to the score
    if (diceTwo >= 4):
        score= score +diceTwo**2
    else:
        score= score-(diceTwo**2)
        #here the score for the t dhirdie is added to the score
    if (diceThree >= 4):
        score= score +diceThree**2
    else:
        score= score-(diceThree**2)
        # the 18 dollar playing fee is subtracted
    score = score-18
    #here a responseis given telling the user the outcome, if they won a negative amount it prints you lost, otherwise it prints you won that amount.
    if(score>0):
        print('You get '+ str(score) +' dollars')
    else:
         print('You lose '+ str(score*-1) +' dollars')

if(__name__=="__main__"):
    main()
