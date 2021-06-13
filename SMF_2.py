"""
Rohan Dalal
20 January 2021
IDT
1st Period
SMF_2
"""

import os, sys
import cs50
import random
# project to utilize different methods of priniting a statement
def main():

    fortune = ["A pleasant surprise is waiting for you.", "A new perspective will come with the new year.", "All the effort you are making will ultimately pay off.",]
    name='CMDR Schenck'
    wantFortune = 'yes'
    x = random.randint(0,2)
    part1 = 'If you liked it '
    part2 = 'please give me a 100'
    Whole = part1 + part2
    print("This is a {machineType}, It will {purpose}".format( machineType = "Fortune teller", purpose = "give you a fortune."))
    print('Hi '+ name + ' would you like a fortune?')
    if (wantFortune =='yes'):
        print('Ok here you go')
        print(fortune[x])
    else:
        print('Ok, have a nice day.')

    print(Whole)
    sys.exit(0)

if (__name__ =="__main__"): 
    
    main()
