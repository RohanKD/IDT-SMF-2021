"""
Rohan Dalal
25 March 2021
IDT
1st Period
SMF_22
"""
#Imports here including the module for this
import SMF_20_module
import cs50
import time

#Here the names are simplified so i can use the module easily
fact = SMF_20_module.fact
Perm = SMF_20_module.Perm
Comb = SMF_20_module.Comb
prob_replacement = SMF_20_module.prob_replacement
prob_no_replacement = SMF_20_module.prob_no_replacement


def main():
    #THe while loop where people can ask questions using one of the 5 probability functions are here
    repeat = 0
    while(repeat == 0):
        response = input('What would you like to do, Your options are \n1: factorial\n2: Combination\n3: Permutation\n4: Card Probability with replacement\n5: Card Probability without replacement\n6: exit\n')
        if(response == '1'):
            x = input('What factorial would you like to calculate: ')
            print('...')
            time.sleep(.5)
            print('...')
            time.sleep(.5)
            print(fact(x))
        elif(response == '2'):
            n = int(input('What is n for nCr: '))
            r = int(input('What is r for nCr: '))
            print('...')
            time.sleep(.5)
            print('...')
            time.sleep(.5)
            print(Comb(n, r))
        elif(response == '3'):
            n = int(input('What is n for nPr: '))
            r = int(input('What is r for nPr: '))
            print('...')
            time.sleep(.5)
            print('...')
            time.sleep(.5)
            print(Perm(n, r))
        elif(response == '4'):
            num_of_draws = int(input('What is the number of cards drawn: '))
            card_type = int(input('What is the card type:'))
            print('...')
            time.sleep(.5)
            print('...')
            time.sleep(.5)
            print(prob_replacement(num_of_draws, card_type))
        elif(response == '5'):
            num_of_draws = int(input('What is the number of card drawn: '))
            card_type = int(input('What is the card type: '))
            print('...')
            time.sleep(.5)
            print('...')
            time.sleep(.5)
            print(prob_no_replacement(num_of_draws, card_type))
        elif(response == '6'):
            repeat += 1
        else:
            print('please enter a valide response: a number 1-6')





if(__name__=='__main__'):
    main()

