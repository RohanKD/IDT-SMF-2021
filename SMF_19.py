"""
Rohan Dalal
25 March 2021
IDT
1st Period
SMF_19
"""
# imports here including the module i made
import SMF_18_module
import os, sys
import cs50
import time

def main():
    #Variables are defined, to assisnt with the while loop, and to use the functions from the module easily
    repeat = 0
    geom = SMF_18_module.inf_geom_series
    fin_geom = SMF_18_module.finite_geom_series
    arithmetic = SMF_18_module.sum_arithmetic_series
    #WHile loop where use can keep using the functions til they exit
    while(repeat == 0):
        response = input('Would you like to do a calculation, your options are: 1:sum of inf geom series, 2:sum of finite geom series, 3:sum of arithmetic series. Enter a number from 1 to 4 to choose. Say "5: none"  to exit')
        if(response == '4'):
            repeat += 1
        elif(response== '1'):
            a = float(input('What is the first term'))
            r = float(input('What is the common ratio'))
            time.sleep(1)
            print('hmm...')
            time.sleep(1)
            print(geom(a, r))
        elif(response == '2'):
            a = float(input('What is the first term'))
            r = float(input('What is the common ratio'))
            n = int(input('What is the number of terms'))
            time.sleep(1)
            print('hmm...')
            time.sleep(1)
            print(fin_geom(a, r, n))
        elif(response == '3'):
            a = float(input('What is the first term'))
            d = float(input('What is the common difference'))
            n = int(input('What is the number of terms'))
            time.sleep(1)
            print('hmm...')
            time.sleep(1)
            print(arithmetic(a, d, n))
        else:
            print('please enter a valid response from 1 to 4. 1: sum of inf geom series,  2: sum of inf geom series, 3: sum of arithmetic series, or 4: none')




if(__name__=='__main__'):
    main()
