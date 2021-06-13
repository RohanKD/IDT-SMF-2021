"""
Rohan Dalal
23  February 2021
IDT
1st Period
SMF_12
"""
import cs50
import os,sys
import random

def main():

    print('You can now make a custom magic 8 ball')
    num = int(input('How many responses would you like your Magic 8 ball to have'))
    
    responses=[]
    loopNum=1
    loop=0
    ifCorrect=0
    
    while(loop==0):


        for x in range(0,num):
            y=  input('what is response number ' +str(loopNum))
            responses.append(y)

            if((y.isalpha())== False):
                ifCorrect+=1

            loopNum+=1


        if(ifCorrect==0):
            loop+=1
        else:
            print('Try again: Enter only one-word responses, using only letters')

        loopNum=1
        ifCorrect=0
      

    listNum= random.randint(0, (num-1))
    z= input('What would you like to write before you give the response?')
    print(z+responses[listNum])

if(__name__=='__main__'):
    main()
