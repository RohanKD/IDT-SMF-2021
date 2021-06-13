"""
Rohan Dalal
22  February 2021
IDT
1st Period
SMF_9
"""
import cs50
import os,sys
import random

def main():
    # Here I ask for the inputs and tell teh user what the module does
    print('this will help you multiply 2 numbers,')
    Decimal = input(" Enter a decimal number ")
    Integer = input("Enter an integer.")
    #Here is where the variables are casted in to the rihgt data-type, since inputs are automatically strings
    Decimal = float(Decimal)
    Integer = int(Integer)
    Mult = float( Decimal*Integer)
    #here the answer is given while rereading their inputs
    print('Your first number is '+ str(Decimal)+ ', and your second number is ' +str(Integer) +', so your asnwer is ' + str(Mult))
    print('You can now divide two numbers')
    #here the variables for dividing are defined, and inputs are asked for
    Num1 = input('Enter the first number')
    Num2 = input('Enter the second number')
    # The variables are converted to float from strings
    Num1 = float(Num1)
    Num2 = float(Num2)
    Div = Num1/Num2
    #this defines new variables which will be used to check if the answer is an integer or float.
    x= int(Div)
    y= float(round(Div, 3))
    #The answer is tested whether it is a decimal or a n integer. ANd an answer will be given in those respective data-types.
    if((x-y)==0):
        x=str(x)
        print('Your answer is '+ x)
    else:
        y=str(y)
        print('Your answer is '+ y )




if(__name__=='__main__'):
    main()
