"""
Rohan Dalal
27 January 2021
IDT
1st Period
SMF_8
"""
import cs50
import os,sys
import random

def main():
    print('This is a custom dice roller, coinflipper, it can even give you a random card')
    Choice= input('Would you like to flip a coin, roll dice, or get a random card?')
    if(Choice==' Flip a coin'):
        sides =['heads', 'tails']
        x=random.randint(0,1)
        print('You got ' +sides[x])
    elif(Choice==' roll dice'):
        y= input('Would you Like to roll one or two dice')
        z= int(input('How many sides would you like your dice to have'))
        if(y==' one'):
            x=random.randint(1,z)
            print('You rolled a '+str(x))
        elif(y==' two'):
            a=random.randint(1,z)
            b=random.randint(1,z)
            print('You rolled a '+str(a)+' and a '+str(b))
    elif(Choice==' Get a random card'):
        cards=['Ace', '2', '3', '4', '5','6', '7', '8', '9', '10','Jack', 'Queen', 'King']
        suits=["Spades", "Diamonds", "Clubs", "Hearts"]
        a=cards[random.randint(0,12)]
        b=suits[random.randint(0,3)]
        print('You drew a(n) '+a+' of '+b)
if(__name__=='__main__'):
    main()


