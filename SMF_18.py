"""
Rohan Dalal
25 March 2021
IDT
1st Period
SMF_18
"""
# I imported the module, and other libraries
import SMF_18_module
import os, sys
import cs50
import time

def main():
    #Here the function is used with a wait time to simulate thinking
    geom = SMF_18_module.inf_geom_series
    response = input('Would you like to do a calculation of an infinite geom series, say "yes" or "no" ')
    if(response == 'yes'):
        a = float(input('What is the first term'))
        r = float(input('What is the common ratio'))
        time.sleep(1)
        print('hmm...')
        time.sleep(1)
        print(geom(a, r))
    else:
          print('ok, see you next time')



if(__name__=='__main__'):
    main()
