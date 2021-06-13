"""
Rohan Dalal
20 January 2021
IDT
1st Period
SMF_3
"""
""" Imported libraries are here, I used the random library to generate pseudo random numbers for the random 8 ball statements
Without these libraries I couldn't have done this"""
import os, sys
import cs50
import random
#Pre-processor directivea to maek sure code is compiled right
def main():
    # The description of what my program does
    print('This is a smart Magic 8 ball, FOr some questions it will give a random answer. But for Some questions such as Will Rohan Get a 100 it will say it is certain.')
    # This list contains all the possible predictions of the magic-8 ball.
    Predictions = [ 'As I see it, yes.', ' Don’t count on it.', 'It is certain.', ' It is decidedly so', 'Most likely', 'My sources say no.', 'My reply is no.', ' Outlook not so good.', 'Outlook very good', 'Signs point to yes', 'Very Doubtful', 'Without a doubt', 'yes', 'Definitely yes']
    # This generates the random number and sets it equal to x, this will come in to play later
    x=random.randint(0,13)
    # This is where the user is asked to input a question.
    Question = input('Ask your question without a question mark, and make sure it starts with a space')
    # Here is where The magic 8 ball gives it's predictions, because it is "smart" for certain questions it will always give the same answer
    if (Question==  ' Will Rohan get a 100 on SMF_3'):
        print('It is certain')
    elif(Question==  ' Is CMDR Schenk a good teacher'):
        print('Undoubtedly So')
        #here is where the variable x comes into play, if the question is not one of the two listed above,
    else:
    #it will respond with a randombly selected option from the Predictions list. x is the random number and that number of the list is called
        print(Predictions[x])
if(__name__=='__main__'):
    main()
