"""
Rohan Dalal
27 January 2021
IDT
1st Period
SMF_7
"""
import os, sys
import cs50

def main():
    print('Please sign up with valid information to win a $100 VISA Gift Card')
    firstname = input('Enter your first name')
    lastname = input('Enter your last name')
    age= input('Enter your age')
    gender = input('Enter your gender')
    email = input('Enter your email')
    Sell= input('Can we sell your info')
    print('can you confirm if your info was correct, you are one step closer to you VISA gift card')
    print('First Name:'+firstname)
    print('Last Name:'+lastname)
    print('Age:'+age)
    print('Gender'+gender)
    print('Email Address:'+email)
    print('Can we sell your info:'+Sell)
    Check = input(' Was all your info correct')

    if(Check==' yes'):
        print('To redeem your offer please complete two more tedious offers that may or may not require your credit card info')
    elif(Check==' no'):
        firstname = input('Enter your first name')
        lastname = input('Enter your last name')
        age= input('Enter your age')
        gender = input('Enter your gender')
        email = input('Enter your email')
        Sell= input('Can we sell your info')
        print('can you confirm if your info was correct, you are one step closer to you VISA gift card')
        print('First Name:'+firstname)
        print('Last Name:'+lastname)
        print('Age:'+age)
        print('Gender'+gender)
        print('Email Address:'+email)
        print('Can we sell your info:'+Sell)
        Check = input(' Was all your info correct')

    else:
        print('please enter a valid option such as  yes or no')

if(__name__=='__main__'):
    main()
